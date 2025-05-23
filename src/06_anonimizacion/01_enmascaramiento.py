"""
Ejemplo de enmascaramiento (masking) de datos sensibles en un DataFrame.

El enmascaramiento es una técnica de anonimización que reemplaza parte de los datos 
sensibles con caracteres especiales (como asteriscos), manteniendo visible solo una 
porción mínima del dato original. Por ejemplo:
- "Juan Pérez" -> "J********z"
- "juan.perez@email.com" -> "j******************m"

Ventajas:
- Mantiene cierta legibilidad al conservar algunos caracteres originales
- Es reversible si se guarda la información original en un lugar seguro
- Permite identificar patrones sin exponer datos completos

Desventajas:
- No es una anonimización completa ya que mantiene parte de la información
- Puede ser insuficiente para datos muy sensibles
- Es posible deducir el dato original si el patrón es muy simple

Este script muestra cómo aplicar enmascaramiento básico a nombres y emails en un DataFrame.
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
