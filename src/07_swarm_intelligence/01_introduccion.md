# Inteligencia de Enjambre con Agents SDK

## ¿Qué es la Inteligencia de Enjambre?

La inteligencia de enjambre (swarm intelligence) es un paradigma de computación distribuida que se inspira en el comportamiento colectivo de sistemas descentralizados y auto-organizados, como las colonias de hormigas, los enjambres de abejas o las bandadas de pájaros. En el contexto de la IA, esto se traduce en sistemas donde múltiples agentes inteligentes colaboran para resolver problemas complejos.

Las características principales de la inteligencia de enjambre incluyen:

- **Descentralización**: No existe un control central que dirija las acciones individuales
- **Auto-organización**: El comportamiento colectivo emerge de las interacciones locales
- **Emergencia**: Las soluciones surgen de manera natural sin una programación explícita
- **Adaptabilidad**: El sistema puede responder a cambios en el entorno
- **Escalabilidad**: Puede funcionar con diferentes números de agentes

Los sistemas de inteligencia de enjambre han demostrado ser especialmente efectivos en:

1. Optimización de rutas y logística
2. Búsqueda distribuida de soluciones
3. Clustering y clasificación de datos
4. Coordinación de robots y drones
5. Análisis de redes sociales y comportamientos colectivos

En el desarrollo moderno de IA, la inteligencia de enjambre se implementa mediante agentes autónomos que siguen reglas simples pero que, en conjunto, pueden abordar tareas complejas como el procesamiento de lenguaje natural, la toma de decisiones distribuida o la resolución colaborativa de problemas.

## Agents SDK de OpenAI

El Agents SDK es un framework moderno para construir sistemas multi-agente que permite:
- Crear agentes con roles específicos
- Definir funciones y herramientas para cada agente
- Establecer flujos de trabajo colaborativos
- Manejar el contexto y la transferencia de control entre agentes

## Estructura de los Ejemplos

En este módulo exploraremos:

1. **Agentes Básicos**: Creación y configuración de agentes simples
2. **Colaboración**: Cómo los agentes pueden trabajar juntos
3. **Herramientas**: Uso de funciones y herramientas personalizadas
4. **Flujos de Trabajo**: Patrones comunes de interacción entre agentes
5. **Casos de Uso**: Ejemplos prácticos de sistemas multi-agente

## Requisitos

```bash
pip install openai>=1.0.0
```

## Configuración

Asegúrate de tener configurada tu API key de OpenAI en el archivo `.env`:

```bash
OPENAI_API_KEY=tu-api-key
```

## Notas Importantes

- El Agents SDK es la evolución recomendada del proyecto experimental Swarm
- Cada agente puede tener su propio modelo, instrucciones y conjunto de herramientas
- Los agentes pueden transferir el control entre sí de manera fluida
- El contexto se mantiene y se puede pasar entre agentes 