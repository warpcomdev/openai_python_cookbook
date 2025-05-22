"""
Ejemplo de evaluación automática de respuestas generadas por un modelo LLM.
Se comparan respuestas generadas y de referencia usando:
- Similitud de embeddings (OpenAI): Compara la similitud semántica entre textos 
  usando embeddings de OpenAI. Captura el significado general.
- BLEU (nltk): Métrica de evaluación que compara n-gramas entre la respuesta 
  generada y la referencia. Útil para evaluar traducciones.
- ROUGE (HuggingFace evaluate): Familia de métricas que evalúa la coincidencia
  de secuencias entre textos. Comúnmente usada para evaluar resúmenes.

Cómo interpretar los resultados:
- Similitud de embeddings: Valor entre -1 y 1. Cuanto más cercano a 1,
  mayor similitud semántica entre las respuestas.
- BLEU: Valor entre 0 y 1. Más alto indica mayor coincidencia de n-gramas
  (palabras o frases) entre la respuesta generada y la referencia.
  Útil para traducción o generación literal.
- ROUGE-L: Valor entre 0 y 1. Más alto indica mayor coincidencia de frases
  o secuencias largas entre la respuesta generada y la referencia.
  Útil para tareas de resumen.

Ninguna métrica es perfecta: usa varias y complementa con evaluación
humana si es posible.
"""

import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os
import nltk
import evaluate
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# Descargar el recurso 'punkt' de NLTK si no está disponible
def ensure_punkt():
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        print("Descargando el recurso 'punkt' de NLTK...")
        nltk.download("punkt")
    # Intentar descargar punkt_tab si existe (no es estándar, pero por si acaso)
    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        try:
            nltk.download("punkt_tab")
        except Exception:
            pass


ensure_punkt()

# Respuestas de ejemplo
generada = (
    "La fotosíntesis es el proceso por el cual las plantas convierten la luz "
    "solar en energía química."
)
referencia = (
    "La fotosíntesis permite a las plantas transformar la luz solar en energía "
    "química."
)


# 1. Similitud de embeddings
def get_embedding(text):
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


emb_gen = get_embedding(generada)
emb_ref = get_embedding(referencia)
sim = cosine_similarity(emb_gen, emb_ref)
print(f"Similitud de embeddings: {sim:.2f}")

# 2. BLEU (nltk)
ref_tokens = [nltk.word_tokenize(referencia, language="spanish")]
gen_tokens = nltk.word_tokenize(generada, language="spanish")
bleu = sentence_bleu(
    ref_tokens, gen_tokens, smoothing_function=SmoothingFunction().method1
)
print(f"BLEU: {bleu:.2f}")

# 3. ROUGE (HuggingFace evaluate)
rouge = evaluate.load("rouge")
rouge_result = rouge.compute(predictions=[generada], references=[referencia])
print(f"ROUGE-L: {rouge_result['rougeL']:.2f}")
