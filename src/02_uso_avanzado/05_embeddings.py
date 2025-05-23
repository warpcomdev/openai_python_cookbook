"""
Ejemplo de uso de embeddings con OpenAI.

Los embeddings son representaciones numéricas de texto que capturan su
significado semántico. En este ejemplo:

1. Generamos embeddings para diferentes textos
2. Calculamos la similitud entre ellos
3. Encontramos el texto más similar a una consulta

Los embeddings son útiles para:
- Búsqueda semántica: Convierte textos y consultas en embeddings para encontrar
  documentos similares semánticamente, aunque no compartan palabras exactas
- Clasificación de texto: Genera embeddings de textos de ejemplo y nuevos textos
  para clasificarlos según su similitud con las categorías conocidas
- Recomendaciones: Calcula embeddings de productos/ítems y encuentra los más
  similares para hacer recomendaciones personalizadas
- Análisis de sentimiento: Compara los embeddings del texto con embeddings de
  referencia positivos/negativos para determinar la polaridad

La similitud del coseno es una medida que nos dice qué tan similares son dos
vectores de embeddings. Funciona así:
- Si los vectores son idénticos, la similitud es 1.0
- Si los vectores son completamente diferentes, la similitud es 0.0
- Si los vectores son opuestos, la similitud es -1.0

Existen diferentes métricas para comparar embeddings, cada una con sus
ventajas:

1. Distancia Euclidiana:
- Mide la distancia directa entre dos puntos en el espacio vectorial
- Útil para espacios de baja dimensionalidad
- Sensible a la escala de los vectores

2. Distancia de Manhattan:
- Suma las diferencias absolutas entre las coordenadas
- Más robusta a valores atípicos que la distancia euclidiana
- Útil cuando los cambios incrementales son importantes

3. Similitud de Jaccard:
- Compara conjuntos de características
- Útil para vectores binarios o categóricos
- Ignora la magnitud de las diferencias

4. Correlación de Pearson:
- Mide la relación lineal entre vectores
- Útil para detectar patrones similares
- Invariante a transformaciones lineales
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
    """Obtiene el embedding de un texto usando el modelo
    text-embedding-ada-002.
    """
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calcula la similitud del coseno entre dos vectores de embeddings.

    Args:
        a: Primer vector de embedding
        b: Segundo vector de embedding

    Returns:
        float: Valor entre -1 y 1 que indica la similitud
        - 1.0: Vectores idénticos
        - 0.0: Vectores completamente diferentes
        - -1.0: Vectores opuestos
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Textos de ejemplo
textos = [
    "Python es un lenguaje de programación interpretado y de alto nivel",
    "JavaScript es el lenguaje de programación más usado en desarrollo web",
    "Java es un lenguaje de programación orientado a objetos",
    "La programación funcional se centra en el uso de funciones puras",
]

# Generamos embeddings para cada texto
print("Generando embeddings...")
embeddings = [get_embedding(texto) for texto in textos]

# Mostrar los primeros valores del embedding de cada texto
print("\nPrimeros valores de los embeddings de cada texto:")
for texto, emb in zip(textos, embeddings):
    print(f"\nTexto: {texto}")
    print(f"Embedding (primeros 8 valores): {emb[:8]}")

# Texto de consulta
consulta = "¿Qué lenguaje se usa para desarrollo web?"

# Generamos el embedding de la consulta
embedding_consulta = get_embedding(consulta)
print(f"\nConsulta: {consulta}")
print(f"Embedding de la consulta (primeros 8 valores): {embedding_consulta[:8]}")

# Calculamos la similitud con cada texto
print("\nCalculando similitudes...")
similitudes = [cosine_similarity(embedding_consulta, emb) for emb in embeddings]

# Encontramos el texto más similar
indice_mas_similar = np.argmax(similitudes)
texto_mas_similar = textos[indice_mas_similar]
similitud_maxima = similitudes[indice_mas_similar]

print("\nResultados:")
print(f"Consulta: {consulta}")
print("\nTexto más similar:")
print(f"- {texto_mas_similar}")
print(f"- Similitud: {similitud_maxima:.2f}")

print("\nSimilitudes con todos los textos:")
for texto, similitud in zip(textos, similitudes):
    print(f"\n- {texto}")
    print(f"  Similitud: {similitud:.2f}")
