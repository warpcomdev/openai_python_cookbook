# Subida y validación de datos para fine-tuning

Para subir y validar tu dataset, asegúrate de tener la variable de entorno `OPENAI_API_KEY` configurada.

> **Importante:** Ejecuta los siguientes comandos en el directorio donde se encuentra el archivo `02_ejemplo_dataset.jsonl`.

> **Advertencia:** Si ves un error como `The api_key client option must be set...`, asegúrate de exportar tu clave API en la terminal antes de ejecutar los comandos:
>
> ```bash
> export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
> ```

## Validar el dataset

Valida el formato y la calidad del archivo JSONL con:

```bash
openai tools fine_tunes.prepare_data -f 02_ejemplo_dataset.jsonl
```

Esto revisa el formato y te sugiere mejoras.

> **Nota:** Si ves un error como `prompt column/key is missing` pero tu archivo usa la clave `messages` (formato chat), puedes ignorarlo. Este error solo aplica a datasets para modelos de completions, no para modelos chat como `gpt-3.5-turbo`.

## Subir el archivo

Sube el archivo para fine-tuning con la CLI moderna:

```bash
openai api files.create -f 02_ejemplo_dataset.jsonl --purpose fine-tune
```

Esto sube el archivo y te da un ID que usarás para lanzar el fine-tuning.

**Recuerda:** Todos los comandos funcionarán siempre que la variable `OPENAI_API_KEY` esté definida en tu entorno.

Más información: [OpenAI CLI Docs](https://platform.openai.com/docs/guides/fine-tuning/cli) 