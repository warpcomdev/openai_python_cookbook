"""
Ejemplo de resumen automático de un texto usando chat.completions de OpenAI.

Este script permite elegir la longitud (corto o medio) y el tono del resumen
(niño, experto, etc). Es útil para condensar información y adaptar el resumen
a diferentes audiencias.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

texto = (
    "La inteligencia artificial (IA) es un campo de la informática que se centra "
    "en la creación de sistemas capaces de realizar tareas que normalmente "
    "requieren inteligencia humana. Esto incluye el aprendizaje, el razonamiento, "
    "la resolución de problemas y la comprensión del lenguaje natural."
)

print("Texto original:\n")
print(texto)

# Elegir longitud del resumen
longitud = input("\nElige la longitud del resumen (corto/medio): ").strip().lower()
if longitud == "corto":
    max_tokens = 40
    tipo_resumen = "en una frase breve"
elif longitud == "medio":
    max_tokens = 80
    tipo_resumen = "en un párrafo conciso"
else:
    print("Opción no válida. Usando longitud 'corto' por defecto.")
    max_tokens = 40
    tipo_resumen = "en una frase breve"

# Elegir tono del resumen
tono = input("Elige el tono del resumen (niño, experto, neutro, etc): ").strip().lower()
if tono == "niño":
    tono_prompt = "Explica de forma sencilla, como para un niño."
elif tono == "experto":
    tono_prompt = "Explica con detalle y precisión, como para un experto."
else:
    tono_prompt = "Explica de forma clara y neutra."

print(f"\nConfiguración elegida: longitud='{longitud}', tono='{tono}'\n")

messages = [
    {
        "role": "system",
        "content": f"Eres un asistente que resume textos. {tono_prompt}",
    },
    {"role": "user", "content": f"Resume el siguiente texto {tipo_resumen}:\n{texto}"},
]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, max_tokens=max_tokens
)

print("Resumen:")
print(response.choices[0].message.content.strip())
