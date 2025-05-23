# Módulo 7: Inteligencia de Enjambre con Agents SDK

Este módulo explora el uso del Agents SDK de OpenAI para crear sistemas multi-agente que colaboran entre sí para resolver tareas complejas.

## Estructura del Módulo

1. **Introducción** (`01_introduccion.md`)
   - Conceptos básicos de inteligencia de enjambre
   - Introducción al Agents SDK
   - Configuración y requisitos

2. **Agentes Básicos** (`02_agentes_basicos.py`)
   - Creación de agentes simples
   - Interacción básica entre agentes
   - Ejemplo: Poeta y Traductor

3. **Herramientas Personalizadas** (`03_herramientas_personalizadas.py`)
   - Definición de herramientas para agentes
   - Uso de funciones personalizadas
   - Ejemplo: Analista de Datos

4. **Flujo Colaborativo** (`04_flujo_colaborativo.py`)
   - Trabajo en equipo entre agentes
   - Flujos de trabajo complejos
   - Ejemplo: Investigación, Análisis y Reporte

5. **Triaje Automático en Soporte Técnico** (`05_triaje_agente.py`)
   - Agente de triaje que decide a qué agente especializado derivar una consulta
   - Temática: Soporte técnico de TI (hardware, software, redes)
   - Ejemplo interactivo por consola

## Requisitos

```bash
pip install openai>=1.0.0 python-dotenv
```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto:
```bash
OPENAI_API_KEY=tu-api-key
```

2. Asegúrate de tener Python 3.7+ instalado.

## Ejemplos

### 1. Agentes Básicos
```bash
python src/07_swarm_intelligence/02_agentes_basicos.py
```
Este ejemplo muestra cómo crear dos agentes (un poeta y un traductor) que colaboran para crear y traducir haikus.

### 2. Herramientas Personalizadas
```bash
python src/07_swarm_intelligence/03_herramientas_personalizadas.py
```
Demuestra cómo crear un agente analista con herramientas personalizadas para análisis de datos y generación de gráficos.

### 3. Flujo Colaborativo
```bash
python src/07_swarm_intelligence/04_flujo_colaborativo.py
```
Muestra un flujo de trabajo donde tres agentes (investigador, analista y reportero) colaboran para crear un reporte completo.

### 4. Triaje Automático en Soporte Técnico
```bash
python src/07_swarm_intelligence/05_triaje_agente.py
```
Este ejemplo interactivo permite introducir consultas de soporte técnico (hardware, software, redes) y el agente de triaje decide a qué especialista derivar la consulta. El agente correspondiente responde con una solución o recomendación.

## Mejores Prácticas

1. **Diseño de Agentes**
   - Define roles claros y específicos
   - Proporciona instrucciones detalladas
   - Limita el alcance de cada agente

2. **Herramientas**
   - Crea herramientas específicas y bien documentadas
   - Valida los parámetros de entrada
   - Maneja errores apropiadamente

3. **Flujos de Trabajo**
   - Diseña flujos claros y secuenciales
   - Mantén el contexto entre agentes
   - Implementa mecanismos de recuperación

## Recursos Adicionales

- [Documentación del Agents SDK](https://platform.openai.com/docs/assistants/overview)
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Guía de Mejores Prácticas](https://platform.openai.com/docs/guides/assistants) 