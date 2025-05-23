# Módulo 8: Retrieval-Augmented Generation (RAG)

## ¿Qué es RAG?

Retrieval-Augmented Generation (RAG) es una técnica que combina modelos generativos (como GPT) con sistemas de recuperación de información. Esta tecnología permite mejorar significativamente las capacidades de los modelos de lenguaje al integrar dos componentes clave:

1. Un modelo generativo base que contiene conocimiento general entrenado previamente
2. Un sistema de recuperación que puede acceder y extraer información específica de fuentes externas

RAG permite que el modelo:
- Responda preguntas consultando documentación actualizada
- Genere texto basado en fuentes verificables 
- Combine el conocimiento general del modelo con datos específicos
- Reduzca las alucinaciones al anclar las respuestas en información real
- Mantenga el contexto actualizado sin necesidad de reentrenar

La información externa puede provenir de diversas fuentes como bases de datos, documentos PDF, sitios web, wikis internas, o cualquier corpus de texto estructurado o no estructurado. El sistema recupera de forma dinámica los fragmentos más relevantes para cada consulta.

## ¿Para qué sirve?
- Responder preguntas sobre documentos propios
- Crear asistentes con conocimiento actualizado
- Buscar información relevante y generar respuestas personalizadas
- Mejorar la precisión y actualidad de los modelos generativos

## Componentes básicos de un sistema RAG
1. **Indexado de documentos:** Se procesan e indexan los textos o documentos de referencia.
2. **Recuperación de contexto:** Ante una consulta, se buscan los fragmentos más relevantes usando búsqueda semántica (embeddings).
3. **Generación aumentada:** El modelo generativo (GPT) recibe la consulta y el contexto recuperado para generar una respuesta informada.

## Casos de uso típicos
- Chatbots con conocimiento de base documental
- Sistemas de preguntas y respuestas sobre manuales, FAQs, PDFs, etc.
- Asistentes empresariales con acceso a información interna

## Requisitos para los ejemplos

```bash
pip install openai>=1.0.0 python-dotenv numpy
```

- Tener una clave de API de OpenAI en el archivo `.env` como en los módulos anteriores.
- Python 3.7+

---

En los siguientes ejemplos verás cómo construir un sistema RAG básico paso a paso. 