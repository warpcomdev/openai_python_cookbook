"""
Ejemplo: Envío de un CSV anonimizado a OpenAI para análisis o resumen.

Este script lee un archivo CSV, anonimiza columnas sensibles (nombre, email),
y envía el contenido anonimizado a GPT-4o para obtener un resumen o análisis.
"""

import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta al CSV de ejemplo (puedes cambiarlo por tu propio archivo)
csv_path = "src/05_multimodal/ejemplo.csv"


# Leer y anonimizar el CSV
def anonimizar_csv(ruta):
    df = pd.read_csv(ruta)
    # Anonimizar columnas comunes (ajusta según tu caso)
    for col in df.columns:
        if "nombre" in col.lower():
            df[col] = "[ANON]"
        if "email" in col.lower():
            df[col] = "anon@example.com"
    return df


csv_anon = anonimizar_csv(csv_path)
print("CSV anonimizado (primeras filas):\n")
print(csv_anon.head())

# Convertir a texto para enviar a OpenAI (máx. 2000 caracteres)
csv_texto = csv_anon.to_csv(index=False)[:2000]

pregunta = "¿Qué patrones interesantes ves en estos datos? Resume brevemente."

messages = [
    {"role": "system", "content": "Eres un asistente que analiza datos tabulares."},
    {
        "role": "user",
        "content": f"Datos CSV (anonimizados):\n{csv_texto}\n\nPregunta: {pregunta}",
    },
]

response = client.chat.completions.create(
    model="gpt-4o", messages=messages, max_tokens=200
)

print("\nRespuesta de OpenAI:")
print(response.choices[0].message.content.strip())
