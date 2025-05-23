"""
Chat interactivo en terminal con OpenAI (gpt-4o-mini).
Permite definir el prompt del sistema y mantener una conversación.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

print("Bienvenido al chat con OpenAI (gpt-4o-mini)")
print("Para salir, escribe 'salir' en cualquier momento.\n")

# Pedir el prompt del sistema
system_prompt = input(
    "Introduce el prompt del sistema (ejemplo: 'Eres un asistente útil y conciso'): "
)
if not system_prompt.strip():
    system_prompt = "Eres un asistente útil y conciso."

# Inicializar historial de mensajes
messages = [{"role": "system", "content": system_prompt.strip()}]

while True:
    user_input = input("Tú: ")
    if user_input.strip().lower() == "salir":
        print("¡Hasta luego!")
        break
    messages.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages, max_tokens=200
        )
        assistant_reply = response.choices[0].message.content.strip()
        print(f"Asistente: {assistant_reply}\n")
        messages.append({"role": "assistant", "content": assistant_reply})
    except Exception as e:
        print(f"Error al comunicarse con la API: {e}")
        break
