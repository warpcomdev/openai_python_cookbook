"""
Ejemplo avanzado de Retrieval-Augmented Generation (RAG) que permite consultar múltiples documentos PDF simultáneamente.

Este script implementa un sistema RAG que:
1. Procesa una colección completa de archivos PDF desde una carpeta especificada por el usuario
2. Extrae el texto de cada PDF y lo divide en fragmentos manejables
3. Mantiene la trazabilidad del origen de cada fragmento, asociándolo con su PDF fuente
4. Utiliza embeddings para indexar y buscar semánticamente en todo el contenido
5. Ante una pregunta del usuario, recupera los fragmentos más relevantes de cualquier PDF
6. Proporciona transparencia mostrando de qué documento proviene cada fragmento usado
7. Genera una respuesta coherente combinando múltiples fuentes de contexto

Características principales:
- Procesamiento multi-documento: analiza todos los PDFs en una carpeta
- Búsqueda semántica: encuentra información relevante independientemente de coincidencias exactas
- Trazabilidad: identifica el origen de cada pieza de información utilizada
- Contexto múltiple: puede combinar información de diferentes documentos en una sola respuesta
- Transparencia: muestra al usuario las fuentes específicas utilizadas para generar la respuesta

Este enfoque es especialmente útil para:
- Análisis de grandes colecciones de documentos
- Búsqueda de información dispersa en múltiples fuentes
- Generación de respuestas que requieren sintetizar información de varios documentos

Requisitos adicionales:
    pip install pymupdf tqdm

path: src/08_rag/pdfs
¿Qué tecnologías son necesarias para sobrevivir en Marte?
¿Cuáles son las diferencias entre las misiones tripuladas y no tripuladas?
¿Qué propone Elon Musk para colonizar Marte?
"""

import os
import numpy as np
import fitz  # pymupdf
from tqdm import tqdm
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

client = OpenAI()


# --- Utilidades PDF y texto ---
def extraer_texto_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto


def dividir_en_chunks(texto, max_palabras=80):
    palabras = texto.split()
    chunks = [
        " ".join(palabras[i : i + max_palabras])
        for i in range(0, len(palabras), max_palabras)
    ]
    return [c for c in chunks if len(c.split()) > 10]


# --- Embeddings y búsqueda ---
def obtener_embedding(texto):
    resp = client.embeddings.create(input=texto, model="text-embedding-3-small")
    return np.array(resp.data[0].embedding)


def buscar_fragmentos_relevantes(pregunta, fragmentos, n=3):
    emb_pregunta = obtener_embedding(pregunta)
    emb_frags = [obtener_embedding(f["texto"]) for f in fragmentos]
    similitudes = [
        np.dot(emb_pregunta, emb_frag)
        / (np.linalg.norm(emb_pregunta) * np.linalg.norm(emb_frag))
        for emb_frag in emb_frags
    ]
    idxs = np.argsort(similitudes)[-n:][::-1]
    return [(fragmentos[i], similitudes[i]) for i in idxs]


# --- Generación con contexto ---
def responder_con_contexto(pregunta, fragmentos):
    contexto = "\n".join(
        [f"[{frag['origen']}] {frag['texto']}" for frag, _ in fragmentos]
    )
    prompt = (
        "Responde a la pregunta usando solo la información dada.\n"
        f"\nContexto:\n{contexto}\n"
        f"\nPregunta: {pregunta}\n"
        "\nRespuesta:"
    )
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.2,
    )
    return respuesta.choices[0].message.content.strip()


# --- Main ---
def main():
    carpeta = input("Introduce la ruta de la carpeta con PDFs: ").strip()
    n = input(
        "¿Cuántos fragmentos relevantes quieres recuperar? (por defecto 3): "
    ).strip()
    n = int(n) if n.isdigit() and int(n) > 0 else 3
    pdfs = [f for f in os.listdir(carpeta) if f.lower().endswith(".pdf")]
    if not pdfs:
        print("No se encontraron PDFs en la carpeta.")
        return
    print(f"Procesando {len(pdfs)} PDFs...")
    fragmentos = []
    for pdf in tqdm(pdfs, desc="Extrayendo PDFs"):
        texto = extraer_texto_pdf(os.path.join(carpeta, pdf))
        for chunk in dividir_en_chunks(texto):
            fragmentos.append({"origen": pdf, "texto": chunk})
    print(f"Fragmentos indexados: {len(fragmentos)}")
    print("\nHaz una pregunta sobre el contenido de los PDFs (o escribe 'salir'):")
    while True:
        pregunta = input("\nPregunta: ").strip()
        if pregunta.lower() == "salir":
            print("Saliendo del sistema RAG multi-PDF.")
            break
        frags_relevantes = buscar_fragmentos_relevantes(pregunta, fragmentos, n=n)
        print("\nFragmentos recuperados:")
        for i, (frag, score) in enumerate(frags_relevantes, 1):
            print(f"{i}. [{frag['origen']}] (similitud {score:.2f})\n{frag['texto']}\n")
        respuesta = responder_con_contexto(pregunta, frags_relevantes)
        print("\nRespuesta del sistema:")
        print(respuesta)


if __name__ == "__main__":
    main()
