"""
Ejemplo de supresión de columnas sensibles en un DataFrame.

La supresión es una técnica de anonimización que elimina completamente columnas o registros
que contienen información sensible o identificadores directos. Por ejemplo:
- Eliminar columnas como email, teléfono o DNI
- Eliminar registros completos que sean demasiado identificables

Ventajas:
- Es la técnica más segura ya que elimina completamente la información sensible
- Simple de implementar y entender
- No requiere gestionar mapeos o transformaciones

Desventajas:
- Pérdida total de la información eliminada
- Puede afectar significativamente la utilidad de los datos
- No es reversible

Este script muestra cómo aplicar supresión eliminando una columna sensible (email) de un DataFrame.
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
