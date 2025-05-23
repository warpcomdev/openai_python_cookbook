"""
Ejemplo de manejo de errores comunes con la API de OpenAI.
Este script demuestra diferentes tipos de errores que pueden ocurrir:
1. API key inválida
2. Modelo inexistente
3. Mensaje mal formateado
4. Límite de tokens excedido
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 1. Error con API key inválida
print("\n1. Probando con API key inválida:")
try:
    client_invalid = OpenAI(api_key="sk-invalid-key")
    response = client_invalid.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": "Hola"}]
    )
except Exception as e:
    print(f"Error esperado: {e}")

# 2. Error con modelo inexistente
print("\n2. Probando con modelo inexistente:")
try:
    response = client.chat.completions.create(
        model="modelo-que-no-existe", messages=[{"role": "user", "content": "Hola"}]
    )
except Exception as e:
    print(f"Error esperado: {e}")

# 3. Error con mensaje mal formateado
print("\n3. Probando con mensaje mal formateado:")
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "invalid_role", "content": "Hola"}],  # role inválido
    )
except Exception as e:
    print(f"Error esperado: {e}")

# 4. Error con límite de tokens excedido
print("\n4. Probando con límite de tokens excedido:")
try:
    # Generamos un texto muy largo
    long_text = "Hola " * 10000
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": long_text}],
        max_tokens=1,
    )
except Exception as e:
    print(f"Error esperado: {e}")

# 5. Llamada exitosa
print("\n5. Probando llamada exitosa:")
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": "Hola"}]
    )
    print("Respuesta exitosa:")
    print(response.choices[0].message.content.strip())
except Exception as e:
    print(f"Error inesperado: {e}")
