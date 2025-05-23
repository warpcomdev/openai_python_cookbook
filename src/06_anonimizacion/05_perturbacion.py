"""
Ejemplo de perturbación (aleatorización) de datos numéricos en un DataFrame.

La perturbación es una técnica de anonimización que añade "ruido" aleatorio a valores
numéricos para dificultar la identificación de valores exactos. Por ejemplo:
- Añadir una pequeña variación aleatoria a importes monetarios
- Modificar ligeramente coordenadas geográficas
- Ajustar fechas/horas en un rango pequeño

Ventajas:
- Mantiene la distribución estadística general de los datos
- Dificulta la identificación de valores específicos
- Permite análisis de tendencias y patrones

Desventajas:
- No es adecuada para datos categóricos o identificadores
- El nivel de ruido debe equilibrarse para mantener utilidad
- Puede afectar a cálculos que requieran valores exactos

Este script muestra cómo aplicar perturbación gaussiana a importes monetarios.
La perturbación gaussiana añade ruido aleatorio siguiendo una distribución normal,
donde la mayoría de las variaciones son pequeñas (cercanas a la media) y las 
variaciones grandes son menos probables, lo que ayuda a preservar mejor las 
propiedades estadísticas de los datos originales.
"""

import pandas as pd
import numpy as np

data = {
    "compra_total": [120.5, 89.99, 210.0, 45.75, 150.2],
}
df = pd.DataFrame(data)

print("Original:\n", df)

np.random.seed(42)
df_pert = df.copy()
df_pert["compra_total"] = df["compra_total"] + np.random.normal(0, 5, len(df))

print("\nPerturbado:\n", df_pert)
