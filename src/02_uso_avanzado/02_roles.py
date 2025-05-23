"""
Ejemplo de uso de roles en una conversación con OpenAI.

Los mensajes en el chat tienen diferentes roles:
- "system": Define el comportamiento y personalidad del asistente
- "user": Contiene las preguntas o instrucciones del usuario
- "assistant": Contiene las respuestas del modelo y es crucial para mantener
  el contexto de la conversación

Este ejemplo demuestra cómo mantener una conversación coherente con múltiples
turnos. La clave está en guardar cada respuesta del modelo con el rol
"assistant" y enviar todo el historial en cada llamada. Esto permite que el
modelo:
- Recuerde lo que se ha dicho anteriormente
- Haga referencias a puntos mencionados antes
- Mantenga el hilo de la conversación de manera natural
- Proporcione respuestas contextuales y coherentes
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Iniciamos la conversación con el mensaje del sistema
messages = [
    {"role": "system", "content": "Eres un asistente útil y conciso."},
]

# Primer turno de la conversación
messages.append(
    {
        "role": "user",
        "content": "¿Cuáles son los 3 lenguajes de programación más populares?",
    }
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=50,
    temperature=0.2,
)

# Guardamos la respuesta del asistente en el historial
assistant_response = response.choices[0].message.content.strip()
messages.append({"role": "assistant", "content": assistant_response})

print("Primera respuesta:")
print(assistant_response)
print("\n" + "-" * 50 + "\n")

# Segundo turno de la conversación
messages.append(
    {
        "role": "user",
        "content": "¿Cuál de esos lenguajes es el más fácil de aprender?",
    }
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,  # Enviamos todo el historial de la conversación
    max_tokens=50,
    temperature=0.2,
)

# Guardamos la nueva respuesta del asistente
assistant_response = response.choices[0].message.content.strip()
messages.append({"role": "assistant", "content": assistant_response})

print("Segunda respuesta:")
print(assistant_response)
print("\n" + "-" * 50 + "\n")

# Mostramos el historial completo de la conversación
print("Historial completo de la conversación:")
for msg in messages:
    print(f"\n{msg['role'].upper()}: {msg['content']}")
