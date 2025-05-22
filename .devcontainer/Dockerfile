FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Instalar dependencias del sistema mínimas necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos del proyecto desde el contexto (la raíz) al contenedor
COPY ../requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY ../src ./src
COPY ../tests ./tests
COPY ../README.md ./README.md

# Exponer el puerto por defecto (ajustable según la app)
EXPOSE 8000

# Comando por defecto (puedes personalizar según tu punto de entrada)
CMD ["python", "-m", "src.example"]
