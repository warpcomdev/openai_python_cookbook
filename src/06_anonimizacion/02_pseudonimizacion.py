"""
Ejemplo de pseudonimización de identificadores en un DataFrame.
"""

import pandas as pd

data = {
    "nombre": ["Juan Pérez", "Ana López", "Carlos Ruiz"],
    "ciudad": ["Madrid", "Barcelona", "Madrid"],
}
df = pd.DataFrame(data)

print("Original:\n", df)

df_pseudo = df.copy()
df_pseudo["nombre"] = [f"Usuario_{i+1:03d}" for i in range(len(df))]
ciudades = {c: f"Ciudad_{i+1:02d}" for i, c in enumerate(df["ciudad"].unique())}
df_pseudo["ciudad"] = df["ciudad"].map(ciudades)

print("\nPseudonimizado:\n", df_pseudo)
