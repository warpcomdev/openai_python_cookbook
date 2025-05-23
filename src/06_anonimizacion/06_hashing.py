"""
Ejemplo de hashing de datos sensibles en un DataFrame.

El hashing es una técnica de anonimización que transforma datos sensibles en una cadena 
de caracteres fija mediante una función hash criptográfica. Por ejemplo:
- "juan.perez@email.com" -> "7d793037a0760186574b0282f2f435e7..."
- "123-45-6789" -> "9d4e1e23f5baa3..."

Ventajas:
- Transformación irreversible (no se puede recuperar el dato original)
- Mismo valor de entrada siempre genera el mismo hash
- Muy difícil generar colisiones (dos entradas con mismo hash)

Desventajas:
- Pérdida total del dato original
- No permite análisis del contenido hasheado
- Los hashes son muy diferentes incluso para entradas similares

Este script muestra cómo aplicar hashing SHA-256 a emails en un DataFrame para
anonimizarlos de forma segura e irreversible.
"""

import pandas as pd
import hashlib

data = {
    "email": ["juan.perez@email.com", "ana.lopez@email.com"],
}
df = pd.DataFrame(data)

print("Original:\n", df)


def hash_valor(valor):
    return hashlib.sha256(valor.encode()).hexdigest()


df_hash = df.copy()
df_hash["email"] = df["email"].apply(hash_valor)

print("\nHasheado:\n", df_hash)
