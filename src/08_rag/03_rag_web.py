"""
Ejemplo de RAG sobre una página de Wikipedia.

- El usuario introduce una URL de Wikipedia.
- El script descarga el texto principal de la página.
- Divide el texto en fragmentos/chunks.
- Indexa los fragmentos usando embeddings de OpenAI.
- Permite hacer preguntas sobre el contenido de la web.
- Recupera el fragmento más relevante y responde usando GPT con ese contexto.

Requisitos adicionales:
    pip install requests beautifulsoup4

https://es.wikipedia.org/wiki/Giro_de_Italia_2025
"""

import re
import numpy as np
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

client = OpenAI()


# --- Utilidades de texto ---
def limpiar_texto(texto):
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def extraer_texto_wikipedia(url):
    """Descarga y extrae el texto principal de una página de Wikipedia."""
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    # Extraer solo los párrafos principales
    parrafos = soup.select("#mw-content-text p")
    texto = " ".join([p.get_text() for p in parrafos])
    return limpiar_texto(texto)


def dividir_en_chunks(texto, max_palabras=80):
    """Divide el texto en fragmentos de hasta max_palabras palabras."""
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


def buscar_fragmento_relevante(pregunta, chunks):
    emb_pregunta = obtener_embedding(pregunta)
    emb_chunks = [obtener_embedding(chunk) for chunk in chunks]
    similitudes = [
        np.dot(emb_pregunta, emb_chunk)
        / (np.linalg.norm(emb_pregunta) * np.linalg.norm(emb_chunk))
        for emb_chunk in emb_chunks
    ]
    idx = int(np.argmax(similitudes))
    return chunks[idx], similitudes[idx]


# --- Generación con contexto ---
def responder_con_contexto(pregunta, contexto):
    prompt = (
        "Responde a la pregunta usando solo la información dada.\n"
        f"\nContexto: {contexto}\n"
        f"\nPregunta: {pregunta}\n"
        "\nRespuesta:"
    )
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.2,
    )
    return respuesta.choices[0].message.content.strip()


# --- Main ---
def main():
    print("Ejemplo RAG sobre Wikipedia.")
    url = input("Introduce la URL de Wikipedia: ").strip()
    print("Descargando y procesando la página...")
    texto = extraer_texto_wikipedia(url)
    if not texto or len(texto) < 100:
        print("No se pudo extraer suficiente texto de la página.")
        return
    print(f"Texto extraído: {len(texto)} caracteres.")
    chunks = dividir_en_chunks(texto)
    print(f"Fragmentos generados: {len(chunks)}")
    print("\nHaz una pregunta sobre el contenido (o escribe 'salir'):")
    while True:
        pregunta = input("\nPregunta: ").strip()
        if pregunta.lower() == "salir":
            print("Saliendo del sistema RAG web.")
            break
        contexto, score = buscar_fragmento_relevante(pregunta, chunks)
        print(f"\nFragmento recuperado (similitud {score:.2f}):\n{contexto}")
        respuesta = responder_con_contexto(pregunta, contexto)
        print("\nRespuesta del sistema:")
        print(respuesta)


if __name__ == "__main__":
    main()
