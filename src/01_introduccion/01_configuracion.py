"""
Configuración inicial y verificación de la API key de OpenAI.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno desde .env
load_dotenv()

# Verificar que existe la API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "No se encontró la API key de OpenAI. "
        "Asegúrate de tener un archivo .env con OPENAI_API_KEY=tu-api-key"
    )

# Inicializar el cliente de OpenAI
client = OpenAI()

# Verificar la conexión con una llamada simple
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hola"}],
        max_tokens=5,
    )
    print("✅ Conexión exitosa con la API de OpenAI")
except Exception as e:
    print(f"❌ Error al conectar con la API de OpenAI: {e}")
    raise
