"""
Ejemplo de perturbación (aleatorización) de datos numéricos en un DataFrame.
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
