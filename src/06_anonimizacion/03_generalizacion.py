"""
Ejemplo de generalización de datos en un DataFrame.

La generalización es una técnica de anonimización que reemplaza valores específicos
por categorías o rangos más amplios. Por ejemplo:
- Edad exacta -> Rango de edad (ej: "30-39")
- Ciudad específica -> Región o país (ej: "España")

Ventajas:
- Reduce la granularidad de los datos preservando su utilidad para análisis
- Dificulta la identificación de individuos específicos
- Mantiene la validez estadística de los datos

Desventajas:
- Pérdida de precisión en los datos
- Puede afectar a análisis que requieran valores exactos
- El nivel de generalización debe equilibrar privacidad y utilidad

Este script muestra cómo aplicar generalización a edades y ubicaciones en un DataFrame.
"""

import pandas as pd

data = {
    "edad": [18, 25, 34, 41, 52],
    "ciudad": ["Madrid", "Barcelona", "Madrid", "Sevilla", "Bilbao"],
}
df = pd.DataFrame(data)

print("Original:\n", df)

df_gen = df.copy()
df_gen["edad"] = pd.cut(
    df["edad"],
    bins=[0, 19, 29, 39, 49, 100],
    labels=["0-19", "20-29", "30-39", "40-49", "50+"],
)
df_gen["ciudad"] = "España"

print("\nGeneralizado:\n", df_gen)
