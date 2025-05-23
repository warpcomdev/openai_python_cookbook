"""
Ejemplo de pseudonimización de identificadores en un DataFrame.

La pseudonimización es una técnica de anonimización que reemplaza los identificadores 
originales por códigos o identificadores artificiales de forma consistente. Por ejemplo:
- "Juan Pérez" -> "Usuario_001" 
- "Madrid" -> "Ciudad_01"

Ventajas:
- Mantiene la consistencia de los datos (el mismo valor original siempre se mapea al mismo pseudónimo)
- Permite análisis de patrones y relaciones entre registros
- Es reversible si se guarda el mapeo original en un lugar seguro

Desventajas:
- No es una anonimización completa ya que existe un mapeo 1:1 con los datos originales
- Requiere gestionar y proteger la tabla de mapeo de forma segura
- Puede ser insuficiente para datos muy sensibles

Este script muestra cómo aplicar pseudonimización básica a nombres y ciudades en un DataFrame.
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
