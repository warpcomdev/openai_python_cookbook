"""
Ejemplo de supresión de columnas sensibles en un DataFrame.
"""

import pandas as pd

data = {
    "nombre": ["Juan Pérez", "Ana López"],
    "email": ["juan.perez@email.com", "ana.lopez@email.com"],
    "ciudad": ["Madrid", "Barcelona"],
}
df = pd.DataFrame(data)

print("Original:\n", df)

df_sin_email = df.drop(columns=["email"])

print("\nSin columna email:\n", df_sin_email)
