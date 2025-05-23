"""
Ejemplo básico de cómo hacer una llamada a la API de OpenAI usando completions.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno (.env)
load_dotenv()

# Obtener la API key y crear el cliente
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

prompt = "Cuéntame un chiste corto."

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
)

print("Respuesta del modelo:")
print(response.choices[0].text.strip())
