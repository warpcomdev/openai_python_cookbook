# Buenas prácticas y limitaciones en la evaluación

- Usa métricas automáticas para comparar rápidamente muchos resultados, pero no confíes solo en ellas
- Complementa siempre con evaluación humana para aspectos subjetivos
- Elige métricas adecuadas para cada tarea (BLEU/ROUGE para generación, F1 para clasificación, etc.)
- Documenta el proceso de evaluación y los criterios usados
- Ten en cuenta el sesgo de los anotadores humanos
- Repite la evaluación si cambias el modelo o los datos
- No sobreoptimices para una métrica concreta: busca un equilibrio 