"""
Ejemplo básico de uso de la API de OpenAI.
"""

import os
import json
from typing import Dict, Any

import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def format_response(response: Dict[str, Any]) -> str:
    """
    Formatea la respuesta de la API para una mejor legibilidad.

    Args:
        response: La respuesta de la API en formato diccionario

    Returns:
        str: Respuesta formateada
    """
    # Extraer el contenido del mensaje
    content = response["choices"][0]["message"]["content"]

    # Crear un diccionario con la información relevante
    formatted_info = {
        "Modelo": response["model"],
        "Tokens usados": {
            "Prompt": response["usage"]["prompt_tokens"],
            "Completado": response["usage"]["completion_tokens"],
            "Total": response["usage"]["total_tokens"],
        },
        "Respuesta": content,
    }

    # Convertir a JSON con indentación
    return json.dumps(formatted_info, indent=2, ensure_ascii=False)


def get_completion(prompt: str, model: str = "gpt-3.5-turbo") -> Dict[str, Any]:
    """
    Obtiene una completación de la API de OpenAI.

    Args:
        prompt: El texto de entrada para la API
        model: El modelo a utilizar

    Returns:
        Dict con la respuesta de la API
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY no encontrada en las variables de entorno")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data
    )

    return response.json()


if __name__ == "__main__":
    # Ejemplo de uso
    try:
        response = get_completion("Hola, ¿cómo estás?")
        print(format_response(response))
    except Exception as e:
        print(f"Error: {e}")
