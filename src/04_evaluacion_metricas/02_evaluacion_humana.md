# Evaluación humana de modelos LLM
La evaluación humana es fundamental para medir aspectos subjetivos como la utilidad, claridad o naturalidad de las respuestas. A diferencia de las métricas automáticas, la evaluación por humanos permite capturar matices y aspectos cualitativos que son difíciles de medir computacionalmente.

Los evaluadores humanos pueden:
- Juzgar si una respuesta es realmente útil y relevante para la pregunta
- Detectar errores sutiles o inconsistencias en el contenido
- Evaluar la fluidez y naturalidad del lenguaje
- Identificar sesgos o contenido inapropiado
- Proporcionar retroalimentación cualitativa detallada

Sin embargo, es importante tener en cuenta que la evaluación humana también tiene sus desafíos, como la subjetividad entre evaluadores, el tiempo y costo requerido, y la necesidad de establecer criterios claros y consistentes.

## ¿Cómo diseñar una evaluación humana?
- Define criterios claros (ej: corrección, utilidad, naturalidad)
- Usa escalas simples (ej: 1-5, sí/no)
- Proporciona ejemplos de buenas y malas respuestas
- Usa una tabla o formulario para que los anotadores registren sus evaluaciones

## Ejemplo de criterios
- ¿La respuesta es correcta?
- ¿Es útil para el usuario?
- ¿Está bien redactada y es natural?

## Plantilla de tabla para anotadores
| ID | Pregunta | Respuesta generada | Corrección (1-5) | Utilidad (1-5) | Naturalidad (1-5) | Comentarios |
|----|----------|--------------------|------------------|----------------|------------------|-------------|
| 1  | ...      | ...                |                  |                |                  |             |

Puedes usar Google Sheets, Excel o cualquier herramienta colaborativa para facilitar la anotación.

---

## ¿Qué hacer después de rellenar la tabla?

- Calcula la media (o mediana) de cada criterio para cada modelo o sistema evaluado.
- Compara los resultados entre modelos para ver cuál es mejor en cada aspecto.
- Analiza los comentarios cualitativos para identificar patrones, errores frecuentes o puntos fuertes.
- Resume los resultados en un informe o presentación, incluyendo ejemplos y recomendaciones.

Esto te permitirá tomar decisiones informadas sobre qué modelo desplegar o cómo mejorarlo. 