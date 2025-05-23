# Módulo 8: Retrieval-Augmented Generation (RAG)

Este módulo explora cómo construir sistemas RAG en Python combinando modelos de lenguaje de OpenAI con recuperación semántica de información desde documentos propios (textos, webs, PDFs, etc.).

## Estructura del Módulo

1. **Introducción** (`01_introduccion.md`)
   - Conceptos y fundamentos de RAG
   - Casos de uso y ventajas

2. **RAG Básico** (`02_rag_basico.py`)
   - Ejemplo simple sobre una base de textos
   - Recuperación y generación con contexto

3. **RAG sobre Web** (`03_rag_web.py`)
   - Consulta sobre el contenido de una página de Wikipedia
   - Scraping, fragmentación y búsqueda semántica

4. **RAG sobre múltiples PDFs** (`04_rag_multi_pdf.py`)
   - Procesamiento de una carpeta de PDFs
   - Recuperación de múltiples fragmentos relevantes
   - Transparencia de fuentes y contexto combinado

## Requisitos

```bash
pip install openai>=1.0.0 python-dotenv numpy requests beautifulsoup4 pymupdf tqdm
```

- Tener una clave de API de OpenAI en el archivo `.env` como en los módulos anteriores.
- Python 3.7+


## Mejores Prácticas

- Fragmenta los documentos en trozos manejables (chunks) para mejorar la recuperación.
- Mantén la trazabilidad del origen de cada fragmento para transparencia.
- Ajusta el número de fragmentos relevantes según la complejidad de la pregunta.
- Considera almacenar los embeddings para acelerar consultas repetidas.
- Revisa los límites de tokens del modelo al concatenar muchos fragmentos.

## Recursos

- [Documentación OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Documentación OpenAI Chat Completions](https://platform.openai.com/docs/guides/gpt)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) 

---

## Otros ejemplos de RAG que se podrían implementar

- **RAG con almacenamiento persistente:** Guardar los embeddings y fragmentos en disco (pickle, sqlite, FAISS, ChromaDB) para acelerar consultas futuras.
- **RAG sobre múltiples tipos de documentos:** Indexar y consultar TXT, Markdown, HTML, CSV, etc., además de PDFs.
- **RAG multilingüe:** Permitir preguntas y respuestas en varios idiomas, o traducir automáticamente el contexto recuperado.
- **RAG con chunking avanzado:** Probar diferentes tamaños de fragmento, solapamiento, o segmentación por párrafos/secciones.
- **RAG con feedback del usuario:** Permitir que el usuario indique si la respuesta fue útil y ajustar el ranking de fragmentos en base al feedback.
- **RAG con búsqueda híbrida:** Combinar búsqueda semántica (embeddings) y búsqueda por palabras clave para mejorar la recuperación.
- **RAG con scraping de webs arbitrarias:** Permitir consultar cualquier web, no solo Wikipedia, con limpieza y filtrado de contenido.
- **RAG con integración de APIs externas:** Usar resultados de búsqueda en tiempo real o APIs de datos como contexto adicional.
- **RAG con visualización de contexto:** Mostrar visualmente los fragmentos recuperados y su relevancia para la respuesta.
- **RAG para preguntas complejas:** Recuperar y combinar varios fragmentos de diferentes fuentes para respuestas que requieren síntesis. 