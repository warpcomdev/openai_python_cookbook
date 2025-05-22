"""
Uso de un modelo fine-tuned desde Python y comparación con el modelo base.

Reemplaza 'ft:gpt-3.5-turbo-xxx' por el nombre de tu modelo fine-tuned.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

pregunta = "¿Qué es la fotosíntesis?"


# Usar el modelo base
def respuesta_base():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente educativo."},
            {"role": "user", "content": pregunta},
        ],
        max_tokens=100,
    )
    return response.choices[0].message.content.strip()


# Usar el modelo fine-tuned
def respuesta_finetuned():
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-xxx",  # Reemplaza por tu modelo
        messages=[
            {"role": "system", "content": "Eres un asistente educativo."},
            {"role": "user", "content": pregunta},
        ],
        max_tokens=100,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("Respuesta del modelo base:")
    print(respuesta_base())
    print("\nRespuesta del modelo fine-tuned:")
    print(respuesta_finetuned())
