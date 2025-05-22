# Introducción a la Evaluación de Modelos LLM

Evaluar la calidad de las respuestas generadas por modelos de lenguaje es fundamental para saber si cumplen con los objetivos de tu proyecto.

## ¿Por qué evaluar?
- Permite comparar modelos y configuraciones
- Ayuda a detectar errores, sesgos y limitaciones
- Es clave para mejorar la experiencia de usuario

## Tipos de evaluación
- **Automática:** Usa métricas objetivas para comparar respuestas generadas con referencias (BLEU, ROUGE, similitud de embeddings, etc.)
- **Humana:** Personas evalúan la calidad, utilidad o naturalidad de las respuestas

## Métricas automáticas comunes
- **Similitud de embeddings:** Mide qué tan parecidas son dos respuestas a nivel semántico
- **BLEU:** Evalúa la coincidencia de n-gramas (útil en traducción)
- **ROUGE:** Evalúa la coincidencia de n-gramas y frases (útil en resumen)
- **Exact match / Accuracy:** Para tareas de clasificación o QA
- **F1-score:** Para clasificación o extracción de entidades

En este módulo verás ejemplos prácticos de evaluación automática y humana, y aprenderás a interpretar los resultados. 