"""
Prompt Engineering: Técnicas para guiar y optimizar el comportamiento de modelos de lenguaje.

El prompt engineering consiste en diseñar cuidadosamente las instrucciones y el contexto
que se le da a un modelo para obtener respuestas más útiles, precisas y controladas.

Principales técnicas:

1. Instrucciones explícitas:
   - Decirle al modelo exactamente cómo debe responder ("Responde en formato de lista").
2. Ejemplos (Few-shot):
   - Proveer ejemplos de pregunta-respuesta para que el modelo imite el formato o el estilo.
3. Restricciones de formato:
   - Pedir respuestas en tablas, listas, JSON, etc.
4. Rol del sistema:
   - Definir el rol del asistente ("Eres un barista experto").
5. Cadena de pensamiento (Chain-of-Thought):
   - Pedir al modelo que razone paso a paso ("Explica tu razonamiento antes de responder").
6. Preguntas intermedias (Step-by-step):
   - Dividir una tarea compleja en pasos más pequeños y guiar al modelo por cada uno.
7. Prompts negativos:
   - Indicar explícitamente qué NO debe hacer el modelo.
8. Contexto adicional:
   - Proveer información relevante o contexto previo para mejorar la respuesta.

Este script permite elegir una técnica y ver cómo afecta la respuesta del modelo.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

pregunta = "¿Cuáles son los pasos para hacer un café?"

print(
    """
Técnicas disponibles:
1. instrucciones - Instrucciones explícitas (formato de lista)
2. fewshot        - Ejemplo pregunta-respuesta (few-shot)
3. formato        - Respuesta en formato de tabla
4. rol            - Definir el rol del asistente
5. cot            - Cadena de pensamiento (razonamiento paso a paso)
"""
)

tipo = (
    input(
        "Elige la técnica de prompt engineering (instrucciones, fewshot, formato, rol, cot): "
    )
    .strip()
    .lower()
)

if tipo == "instrucciones":
    system_prompt = "Responde siempre en formato de lista numerada."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pregunta},
    ]
elif tipo == "fewshot":
    system_prompt = "Responde de forma breve y clara."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "¿Cuáles son los pasos para hervir agua?"},
        {
            "role": "assistant",
            "content": "1. Llenar una olla con agua.\n2. Colocar la olla en la estufa.\n3. Encender el fuego.\n4. Esperar a que el agua hierva.",
        },
        {"role": "user", "content": pregunta},
    ]
elif tipo == "formato":
    system_prompt = "Responde en formato de tabla con dos columnas: Paso y Descripción."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pregunta},
    ]
elif tipo == "rol":
    system_prompt = (
        "Eres un barista profesional. Explica los pasos con consejos de experto."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pregunta},
    ]
elif tipo == "cot":
    system_prompt = "Responde razonando paso a paso antes de dar la respuesta final."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pregunta},
    ]
else:
    print("Técnica no reconocida. Usando instrucciones explícitas por defecto.")
    system_prompt = "Responde siempre en formato de lista numerada."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pregunta},
    ]

print(f"\nTécnica elegida: {tipo}\n")

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, max_tokens=300
)

print("Respuesta:")
print(response.choices[0].message.content.strip())
