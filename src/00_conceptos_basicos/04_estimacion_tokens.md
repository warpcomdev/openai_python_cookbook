# Estimación de Tokens en OpenAI

Este módulo explica cómo estimar el número de tokens en textos para modelos de OpenAI, lo cual es crucial para gestionar límites de contexto y costes.

## Métodos de Estimación

### 1. Tokenizador Online Oficial de OpenAI

OpenAI ofrece un tokenizador online en su [Playground](https://platform.openai.com/tokenizer).  
- Copia y pega tu texto en el campo de entrada.
- El tokenizador muestra el número de tokens y la segmentación.

### 2. Librería `tiktoken`

La librería oficial `tiktoken` permite estimar tokens programáticamente:

```bash
pip install tiktoken
```

Ejemplo de uso:

```python
import tiktoken

# Selecciona el codificador según el modelo (por ejemplo, "gpt-4")
enc = tiktoken.encoding_for_model("gpt-4")

# Texto a tokenizar
texto = "Hola, ¿cómo estás?"

# Obtener tokens
tokens = enc.encode(texto)
print(f"Número de tokens: {len(tokens)}")
print(f"Tokens: {tokens}")
```

### 3. Estimación desde el Playground o API

- **Playground:** Al escribir en el Playground, OpenAI muestra el contador de tokens en tiempo real.
- **API:** Al enviar una solicitud, la respuesta incluye el número de tokens usados en `usage`.

### 4. Estimación Manual Rápida

- **Regla general:** En inglés, 1 token ≈ 4 caracteres o 0.75 palabras.
- **Español:** Debido a caracteres especiales y palabras más largas, 1 token ≈ 3-4 caracteres o 0.6-0.7 palabras.
- **Fórmula aproximada:**  100 palabras ≈ 75 tokens

## Consideraciones

- Los tokens no son caracteres ni palabras exactas; dependen del modelo y el idioma.
- Los espacios, signos de puntuación y caracteres especiales también se tokenizan.
- La estimación manual es aproximada; usa herramientas oficiales para mayor precisión.

## Recursos

- [Documentación de tiktoken](https://github.com/openai/tiktoken)
- [Playground de OpenAI](https://platform.openai.com/tokenizer)
- [Guía de tokens de OpenAI](https://platform.openai.com/docs/guides/gpt/managing-tokens) 