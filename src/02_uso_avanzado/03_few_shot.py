"""
Ejemplo de Few-Shot Learning con OpenAI.

El Few-Shot Learning es una técnica donde proporcionamos al modelo algunos
ejemplos de entrada y salida antes de hacer nuestra pregunta real. Esto ayuda
al modelo a:

1. Entender el formato esperado de la respuesta
2. Aprender el patrón o tarea específica que queremos que realice
3. Mejorar la precisión de sus respuestas

En este ejemplo, enseñamos al modelo a extraer información estructurada de
reseñas de restaurantes:
- Le mostramos ejemplos de cómo extraer platos, precios y valoraciones
- Luego le pedimos que analice una nueva reseña
- El modelo "aprende" del patrón y aplica la misma lógica

Es como enseñar a alguien con ejemplos: "Si ves una reseña, extrae esta
información en este formato específico. Ahora, analiza esta nueva reseña
siguiendo el mismo patrón."
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Primero, probamos SIN few-shot learning
print("1. Prueba SIN few-shot learning:")
messages_sin_ejemplos = [
    {
        "role": "system",
        "content": (
            "Extrae la información de la reseña en formato JSON con los campos: "
            "platos, precios y valoración (1-5)."
        ),
    },
    {
        "role": "user",
        "content": (
            "Reseña: Fui a este restaurante y probé la paella de marisco (25€) "
            "y el tiramisú (8€). La paella estaba deliciosa, pero el postre era "
            "demasiado dulce. En general, buena experiencia."
        ),
    },
]

response_sin_ejemplos = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages_sin_ejemplos, max_tokens=150
)

print("Respuesta sin ejemplos:")
print(response_sin_ejemplos.choices[0].message.content.strip())
print("\n" + "-" * 50 + "\n")

# Ahora, probamos CON few-shot learning
print("2. Prueba CON few-shot learning:")
messages_con_ejemplos = [
    {
        "role": "system",
        "content": (
            "Extrae la información de la reseña en formato JSON con los campos: "
            "platos, precios y valoración (1-5)."
        ),
    },
    {
        "role": "user",
        "content": (
            "Reseña: Pedí la ensalada César (12€) y el filete (22€). "
            "La ensalada estaba fresca y el filete perfectamente hecho. "
            "Excelente servicio."
        ),
    },
    {
        "role": "assistant",
        "content": """{
    "platos": ["ensalada César", "filete"],
    "precios": [12, 22],
    "valoracion": 5
}""",
    },
    {
        "role": "user",
        "content": (
            "Reseña: Comí la pasta carbonara (15€) y el helado (6€). "
            "La pasta estaba fría y el helado derretido. "
            "No volveré."
        ),
    },
    {
        "role": "assistant",
        "content": """{
    "platos": ["pasta carbonara", "helado"],
    "precios": [15, 6],
    "valoracion": 1
}""",
    },
    {
        "role": "user",
        "content": (
            "Reseña: Fui a este restaurante y probé la paella de marisco (25€) "
            "y el tiramisú (8€). La paella estaba deliciosa, pero el postre era "
            "demasiado dulce. En general, buena experiencia."
        ),
    },
]

response_con_ejemplos = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages_con_ejemplos, max_tokens=150
)

print("Respuesta con ejemplos:")
print(response_con_ejemplos.choices[0].message.content.strip())
print("\n" + "-" * 50 + "\n")

print("Nota: Observa cómo la respuesta con few-shot learning:")
print("1. Sigue exactamente el formato JSON mostrado en los ejemplos")
print("2. Extrae la información de manera más consistente")
print("3. Mantiene la estructura de los campos (platos, precios, valoración)")
print("\nMientras que sin ejemplos, el modelo puede:")
print("1. Dar respuestas más verbosas o menos estructuradas")
print("2. Incluir información adicional no solicitada")
print("3. Usar un formato diferente al JSON")
