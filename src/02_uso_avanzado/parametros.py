"""
Ejemplo de uso de parámetros avanzados con OpenAI (temperature, max_tokens,
stop).

El parámetro 'stop' recibe una lista de strings. Cuando el modelo genera
alguno de esos strings en la respuesta, la generación se detiene inmediatamente
y ese string no aparece en la salida final.

Por ejemplo, stop=["3.", "FIN"] detendrá la generación si el modelo escribe
"3." o "FIN".
Esto es útil para controlar la longitud o el formato de la salida,
especialmente en listas o respuestas estructuradas.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "Eres un asistente útil."},
    {"role": "user", "content": "Genera una lista de animales domésticos."},
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=50,  # Limitar la longitud de la respuesta
    temperature=0.2,  # Respuestas más deterministas
    # El parámetro 'stop' detiene la generación al encontrar "3." o "FIN".
    stop=["3.", "FIN"],
)

print("Respuesta:")
print(response.choices[0].message.content.strip())
