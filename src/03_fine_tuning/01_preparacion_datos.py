"""
Preparación de datos para fine-tuning con OpenAI.

- El dataset debe estar en formato JSONL (JSON Lines),
  donde cada línea es un objeto JSON válido,
  con campos 'messages' (para chat) o 'prompt' y
  'completion' (para completions).
- Cada línea es un ejemplo independiente.
- Es importante limpiar y revisar los datos para evitar errores y sesgos.

Este script muestra cómo crear y validar un pequeño dataset de ejemplo.
"""

import json

# Ejemplo de dataset para fine-tuning de chat (GPT-3.5-turbo)
ejemplos = [
    {
        "messages": [
            {"role": "system", "content": "Eres un asistente educativo."},
            {"role": "user", "content": "¿Qué es la fotosíntesis?"},
            {
                "role": "assistant",
                "content": (
                    "La fotosíntesis es el proceso por el cual las plantas "
                    "convierten la luz solar en energía química."
                ),
            },
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "Eres un asistente educativo."},
            {"role": "user", "content": "Explica la gravedad."},
            {
                "role": "assistant",
                "content": (
                    "La gravedad es una fuerza que atrae los objetos hacia el "
                    "centro de la Tierra o entre sí."
                ),
            },
        ]
    },
]


# Guardar el dataset en formato JSONL
def guardar_jsonl(ejemplos, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        for ejemplo in ejemplos:
            f.write(json.dumps(ejemplo, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    ruta = "02_ejemplo_dataset.jsonl"
    guardar_jsonl(ejemplos, ruta)
    print(f"Dataset de ejemplo guardado en {ruta}")
