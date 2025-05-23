"""
Ejemplo básico de cómo enviar un prompt a un modelo chat de OpenAI (gpt-4o-mini).
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno (.env)
load_dotenv()

# Obtener la API key y crear el cliente
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Definir el prompt y los mensajes
messages = [
    {"role": "system", "content": "Eres un asistente útil y conciso."},
    {"role": "user", "content": "¿Cuál es la capital de Francia?"},
]

# Realizar la llamada al modelo chat
response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, max_tokens=50
)

# Mostrar la respuesta generada
print("Respuesta del modelo:")
print(response.choices[0].message.content.strip())
