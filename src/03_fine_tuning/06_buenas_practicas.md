# Buenas prácticas para fine-tuning y modelos personalizados

- Usa datos limpios, variados y representativos de tu caso de uso
- No incluyas información sensible o privada en los datos
- Empieza con un dataset pequeño y expande según resultados
- Evalúa el modelo con ejemplos reales antes de ponerlo en producción
- Controla el overfitting: el overfitting ocurre cuando el modelo se ajusta demasiado a los datos de entrenamiento y pierde capacidad de generalización. Si el modelo responde de forma muy similar o idéntica a diferentes prompts, es una señal de overfitting y necesitarás añadir más variedad a los datos de entrenamiento
- Versiona tus datasets y modelos para poder comparar resultados
- Documenta los cambios y el propósito de cada modelo fine-tuned
- Revisa los costes y limita el uso si es necesario

Más información: [Fine-tuning OpenAI Docs](https://platform.openai.com/docs/guides/fine-tuning) 