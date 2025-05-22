# Módulo 1: Introducción a la API de OpenAI

Este módulo te guiará a través de los pasos básicos para comenzar a usar la API de OpenAI en Python, incluyendo ejemplos de completions clásicos y chat conversacional.

## Requisitos Previos

1. Python 3.7 o superior
2. Una cuenta en OpenAI (https://platform.openai.com)
3. Una API key de OpenAI

## Instalación

1. Instala las dependencias necesarias:
```bash
pip install openai python-dotenv
```

2. Crea un archivo `.env` en la raíz del proyecto con tu API key:
```
OPENAI_API_KEY=tu-api-key-aquí
```

## Contenido del Módulo

- **configuracion.py**: Configuración del entorno y verificación de la API key.
- **primer_llamada.py**: Ejemplo básico de uso del endpoint completions.
- **chat_terminal.py**: Chat interactivo en terminal usando el endpoint chat.completions.

## Diferencia entre `completions` y `chat.completions`

- **completions**:  
  Es el endpoint clásico para completar texto a partir de un prompt. Se usa principalmente para tareas de generación de texto directo, como completar frases, redactar textos, etc.  
  Ejemplo de uso:  
  ```python
  response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt="Escribe un poema sobre el mar.",
      max_tokens=100
  )
  ```

- **chat.completions**:  
  Es el endpoint optimizado para conversaciones y chatbots. Permite enviar una lista de mensajes con roles (`system`, `user`, `assistant`) y mantiene el contexto conversacional. Es el recomendado para asistentes virtuales, chatbots y tareas donde el contexto de la conversación es importante.  
  Ejemplo de uso:  
  ```python
  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system", "content": "Eres un asistente útil."},
          {"role": "user", "content": "¿Cuál es la capital de Francia?"}
      ],
      max_tokens=50
  )
  ```

> En general, para tareas conversacionales y asistentes, usa `chat.completions`. Si necesitas mantener código legado con modelos antiguos como `text-davinci-003`, puedes usar completions, pero no se recomienda para nuevos desarrollos.

## Ejercicios Prácticos

1. Modifica el prompt en `primer_llamada.py` para generar diferentes tipos de respuestas.
2. Experimenta con diferentes valores de `temperature` para ver cómo afecta a las respuestas.
3. Prueba el chat interactivo y cambia el prompt del sistema para ver cómo cambia el comportamiento del asistente.

## Recursos Adicionales

- [Documentación oficial de OpenAI](https://platform.openai.com/docs/api-reference)
- [Guía de mejores prácticas](https://platform.openai.com/docs/guides/gpt-best-practices)
- [Ejemplos de uso](https://platform.openai.com/examples)
