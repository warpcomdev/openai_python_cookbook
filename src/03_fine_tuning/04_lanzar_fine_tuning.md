# Lanzar un fine-tuning y monitorizar el proceso

Una vez subido el archivo y validado, puedes lanzar el fine-tuning con:

```bash
openai fine_tunes.create -t <ID_DEL_ARCHIVO>
```

Reemplaza `<ID_DEL_ARCHIVO>` por el ID que te dio el comando anterior.

## Ver el estado del fine-tuning

```bash
openai fine_tunes.list
```

## Ver detalles y logs

```bash
openai fine_tunes.follow -i <ID_DEL_FINE_TUNE>
```

Más información: [Fine-tuning OpenAI Docs](https://platform.openai.com/docs/guides/fine-tuning) 