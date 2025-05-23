"""
Ejemplo de generalización de datos en un DataFrame.
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
