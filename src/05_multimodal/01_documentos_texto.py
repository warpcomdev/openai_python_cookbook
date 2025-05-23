"""
Ejemplo: Análisis y preguntas sobre documentos de texto o PDF con OpenAI.

Este script extrae el texto de un PDF y permite hacer preguntas sobre su contenido usando GPT-4o.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import fitz  # PyMuPDF

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta al PDF de ejemplo (puedes cambiarlo por tu propio archivo)
pdf_path = "src/05_multimodal/ejemplo.pdf"


# Extraer texto del PDF
def extraer_texto_pdf(ruta):
    doc = fitz.open(ruta)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto


texto_pdf = extraer_texto_pdf(pdf_path)
print("Texto extraído del PDF (primeros 500 caracteres):\n")
print(texto_pdf[:500])

# Pregunta de ejemplo sobre el PDF
pregunta = "¿De qué trata el documento? Haz un resumen breve."

messages = [
    {
        "role": "system",
        "content": "Eres un asistente que responde preguntas sobre documentos.",
    },
    {
        "role": "user",
        "content": f"Texto del documento:\n{texto_pdf[:2000]}\n\nPregunta: {pregunta}",
    },
]

response = client.chat.completions.create(
    model="gpt-4o", messages=messages, max_tokens=200
)

print("\nRespuesta de OpenAI:")
print(response.choices[0].message.content.strip())
