"""
Ejemplo de hashing de datos sensibles en un DataFrame.
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
