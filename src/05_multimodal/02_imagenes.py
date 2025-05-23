"""
Ejemplo: Análisis y preguntas sobre imágenes con OpenAI (GPT-4o).

Este script envía una imagen a GPT-4o y permite hacer preguntas sobre su contenido.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta a la imagen de ejemplo (puedes cambiarla por tu propia imagen)
image_path = "src/05_multimodal/ejemplo.jpg"


# Cargar y codificar la imagen en base64
def cargar_imagen_base64(ruta):
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


imagen_b64 = cargar_imagen_base64(image_path)

# Pregunta de ejemplo sobre la imagen
pregunta = "¿Qué aparece en la imagen?"

messages = [
    {"role": "system", "content": "Eres un asistente que describe imágenes."},
    {
        "role": "user",
        "content": [
            {"type": "text", "text": pregunta},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{imagen_b64}"},
            },
        ],
    },
]

response = client.chat.completions.create(
    model="gpt-4o", messages=messages, max_tokens=200
)

print("\nRespuesta de OpenAI:")
print(response.choices[0].message.content.strip())
