"""
Ejemplo básico de Retrieval-Augmented Generation (RAG) con OpenAI.

- Indexa una pequeña base de textos.
- Permite al usuario hacer una pregunta.
- Recupera el fragmento más relevante usando embeddings.
- Usa GPT para responder usando el contexto recuperado.
"""

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
client = OpenAI()

# Base de documentos (puedes ampliar o modificar)
documentos = [
    "La capital de Francia es París.",
    "El agua hierve a 100 grados Celsius.",
    "Python es un lenguaje de programación muy popular.",
    "La Gran Muralla China es visible desde el espacio.",
    "El sol es una estrella ubicada en el centro del sistema solar.",
]


def obtener_embedding(texto: str) -> np.ndarray:
    """Obtiene el embedding de un texto usando OpenAI."""
    response = client.embeddings.create(input=texto, model="text-embedding-3-small")
    return np.array(response.data[0].embedding)


def buscar_documento_relevante(pregunta: str, docs: list[str]) -> tuple[str, float]:
    """Devuelve el documento más relevante y su similitud."""
    emb_pregunta = obtener_embedding(pregunta)
    emb_docs = [obtener_embedding(doc) for doc in docs]
    similitudes = [
        np.dot(emb_pregunta, emb_doc)
        / (np.linalg.norm(emb_pregunta) * np.linalg.norm(emb_doc))
        for emb_doc in emb_docs
    ]
    idx = int(np.argmax(similitudes))
    return docs[idx], similitudes[idx]


def responder_con_contexto(pregunta: str, contexto: str) -> str:
    """Genera una respuesta usando GPT y el contexto recuperado."""
    prompt = (
        "Contesta la siguiente pregunta usando solo la información dada.\n"
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


def main():
    print("\nBase de documentos:")
    for i, doc in enumerate(documentos, 1):
        print(f"{i}. {doc}")
    print("\nHaz una pregunta sobre la base de datos (o escribe 'salir'):")
    while True:
        pregunta = input("\nPregunta: ").strip()
        if pregunta.lower() == "salir":
            print("Saliendo del sistema RAG básico.")
            break
        contexto, score = buscar_documento_relevante(pregunta, documentos)
        print(f"\nFragmento recuperado (similitud {score:.2f}): {contexto}")
        respuesta = responder_con_contexto(pregunta, contexto)
        print("\nRespuesta del sistema:")
        print(respuesta)


definir = __name__ == "__main__"
if definir:
    main()
