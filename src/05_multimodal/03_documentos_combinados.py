"""
Ejemplo: Prompt combinado de texto e imagen con OpenAI (GPT-4o).

Este script envía una imagen y un texto adicional a GPT-4o y permite hacer preguntas sobre ambos.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta a la imagen de ejemplo (puedes cambiarla por tu propia imagen)
image_path = "src/05_multimodal/ticket.jpeg"


# Cargar y codificar la imagen en base64
def cargar_imagen_base64(ruta):
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


imagen_b64 = cargar_imagen_base64(image_path)

# Texto adicional (por ejemplo, instrucciones o contexto)
texto_adicional = "Este es el recibo de una compra realizada el 5 de junio de 2024."

# Pregunta de ejemplo sobre el conjunto texto + imagen
pregunta = "¿Cuál es el importe total de la compra que aparece en el recibo?"

messages = [
    {
        "role": "system",
        "content": "Eres un asistente que analiza documentos con texto e imagen.",
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": texto_adicional},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{imagen_b64}"},
            },
            {"type": "text", "text": pregunta},
        ],
    },
]

response = client.chat.completions.create(
    model="gpt-4o", messages=messages, max_tokens=200
)

print("\nRespuesta de OpenAI:")
print(response.choices[0].message.content.strip())
