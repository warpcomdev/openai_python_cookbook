"""
Configuración básica para usar la API de OpenAI.

Este módulo muestra cómo configurar el entorno para usar la API de OpenAI.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


def configurar_api():
    """
    Configura la API key de OpenAI desde variables de entorno.

    Returns:
        bool: True si la configuración fue exitosa, False en caso contrario.
    """
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la API key desde las variables de entorno
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: No se encontró la API key de OpenAI.")
        print("Por favor, crea un archivo .env en la raíz del proyecto y agrega:")
        print("OPENAI_API_KEY=tu-api-key-aquí")
        return False

    return True


def verificar_configuracion():
    """
    Verifica que la configuración de la API sea correcta.

    Returns:
        bool: True si la configuración es correcta, False en caso contrario.
    """
    try:
        # Crear el cliente y verificar la configuración
        client = OpenAI()
        client.models.list()
        print("✅ Configuración exitosa: La API key es válida.")
        return True
    except Exception as e:
        print(f"❌ Error en la configuración: {str(e)}")
        return False


if __name__ == "__main__":
    if configurar_api():
        verificar_configuracion()
