"""
Ejemplo de búsqueda semántica usando embeddings de OpenAI.

El usuario ingresa una consulta y el script devuelve el texto más similar de una lista,
calculando la similitud semántica mediante embeddings y similitud del coseno.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np
from typing import List

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def get_embedding(text: str) -> List[float]:
    """Obtiene el embedding de un texto usando el modelo text-embedding-ada-002."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calcula la similitud del coseno entre dos vectores."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Lista de textos de ejemplo
textos = [
    "El perro duerme en la cama",
    "La capital de Francia es París",
    "Python es un lenguaje de programación popular",
    "El fútbol es el deporte más popular del mundo",
    "La fotosíntesis ocurre en las plantas",
]

# Generar embeddings para los textos
print("Generando embeddings de los textos...")
embeddings = [get_embedding(texto) for texto in textos]

# Solicitar consulta al usuario
consulta = input("\nIntroduce tu consulta: ")
embedding_consulta = get_embedding(consulta)

# Calcular similitud con cada texto
similitudes = [cosine_similarity(embedding_consulta, emb) for emb in embeddings]

# Encontrar el texto más similar
indice_mas_similar = np.argmax(similitudes)
texto_mas_similar = textos[indice_mas_similar]
similitud_maxima = similitudes[indice_mas_similar]

print("\nTexto más similar encontrado:")
print(f"- {texto_mas_similar}")
print(f"- Similitud: {similitud_maxima:.2f}")

print("\nSimilitudes con todos los textos:")
for texto, similitud in zip(textos, similitudes):
    print(f"- {texto}\n  Similitud: {similitud:.2f}")
