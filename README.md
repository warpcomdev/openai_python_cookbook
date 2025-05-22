# OpenAI Cookbook Python

Este proyecto es una colección de ejemplos y recetas para trabajar con la API de OpenAI usando Python.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd openai-cookbook
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Validar la instalación:
```bash
python -m src.validate_env
```

## Estructura del Proyecto

```
.
├── .devcontainer/     # Configuración del contenedor de desarrollo
├── src/              # Código fuente
│   ├── __init__.py
│   ├── example.py    # Ejemplo básico de uso de la API
│   └── validate_env.py # Script de validación del entorno
├── tests/            # Pruebas unitarias
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Este archivo
```

## Desarrollo

Para ejecutar las pruebas:
```bash
pytest
```

Para formatear el código:
```bash
black .
```

Para verificar el estilo del código:
```bash
flake8
```

## Validación del Entorno

El proyecto incluye un script de validación que verifica:
- Versión de Python
- Dependencias instaladas
- Configuración básica

Para ejecutar la validación:
```bash
python -m src.validate_env
```

## Licencia

MIT 