"""
Primera llamada a la API de OpenAI.

Este módulo muestra cómo hacer una llamada básica a la API de OpenAI
usando el modelo de completions.
"""

from openai import OpenAI
from .configuracion import configurar_api


def hacer_primer_llamada(prompt="Cuéntame un chiste corto"):
    """
    Realiza una llamada básica a la API de OpenAI.

    Args:
        prompt (str): El texto que se enviará a la API.

    Returns:
        str: La respuesta generada por el modelo.
    """
    try:
        # Crear el cliente de OpenAI
        client = OpenAI()

        # Realizar la llamada a la API
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Modelo básico para completions
            prompt=prompt,
            max_tokens=100,  # Límite de tokens en la respuesta
            temperature=0.7,  # Controla la creatividad (0.0 a 1.0)
        )

        # Extraer y retornar el texto generado
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error al hacer la llamada a la API: {str(e)}")
        return None


def main():
    """
    Función principal que demuestra el uso básico de la API.
    """
    # Configurar la API
    if not configurar_api():
        return

    # Hacer la primera llamada
    print("\n🤖 Haciendo la primera llamada a la API...")
    respuesta = hacer_primer_llamada()

    if respuesta:
        print("\n📝 Respuesta del modelo:")
        print("-" * 50)
        print(respuesta)
        print("-" * 50)


if __name__ == "__main__":
    main()
