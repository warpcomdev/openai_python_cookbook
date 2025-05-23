"""
Ejemplo de enmascaramiento (masking) de datos sensibles en un DataFrame.
"""

import pandas as pd

data = {
    "nombre": ["Juan Pérez", "Ana López"],
    "email": ["juan.perez@email.com", "ana.lopez@email.com"],
    "ciudad": ["Madrid", "Barcelona"],
}
df = pd.DataFrame(data)

print("Original:\n", df)


def enmascarar(valor):
    if isinstance(valor, str) and len(valor) > 2:
        return valor[0] + "*" * (len(valor) - 2) + valor[-1]
    return valor


df_masked = df.copy()
df_masked["nombre"] = df_masked["nombre"].apply(enmascarar)
df_masked["email"] = df_masked["email"].apply(enmascarar)

print("\nEnmascarado:\n", df_masked)
