# Módulo 3: Fine-tuning y Modelos Personalizados

Este módulo explica cómo adaptar modelos de OpenAI a tareas o dominios específicos mediante fine-tuning (ajuste fino) y el uso de modelos personalizados.

## Contenido

- 00_introduccion.md: ¿Qué es el fine-tuning? Ventajas, limitaciones y cuándo usarlo.
- 01_preparacion_datos.py: Cómo preparar y validar datasets para fine-tuning.
- 02_ejemplo_dataset.jsonl: Ejemplo de dataset en formato JSONL.
- 03_subida_datos.md: Subir y validar archivos con la CLI de OpenAI.
- 04_lanzar_fine_tuning.md: Lanzar un fine-tuning y monitorizar el proceso.
- 05_uso_modelo.py: Usar un modelo fine-tuned desde Python y comparar resultados.
- 06_buenas_practicas.md: Consejos, buenas prácticas y gestión de modelos.

## Requisitos

- Acceso a la API de OpenAI con permisos para fine-tuning
- openai >= 1.0.0 y la CLI de OpenAI incluida
- **IMPORTANTE:** La autenticación se realiza mediante la variable de entorno `OPENAI_API_KEY`.
- No es necesario ejecutar `openai login` con la CLI moderna (>=1.x).

## Recursos útiles

- [Fine-tuning OpenAI Docs](https://platform.openai.com/docs/guides/fine-tuning)
- [OpenAI CLI Docs](https://platform.openai.com/docs/guides/fine-tuning/cli) 