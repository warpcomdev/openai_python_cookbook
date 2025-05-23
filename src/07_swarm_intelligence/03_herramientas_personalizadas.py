"""
Ejemplo de uso de herramientas personalizadas con el Agents SDK.

Este script demuestra cómo crear y usar herramientas personalizadas con los agentes.
Las herramientas permiten que los agentes realicen acciones específicas como:

- Consultar APIs externas
- Realizar cálculos complejos
- Acceder a bases de datos
- Manipular archivos
- Ejecutar funciones personalizadas

Cada herramienta se define con:
- Un nombre único
- Una descripción de su función
- Los parámetros que acepta
- La lógica de ejecución

El script muestra cómo:
1. Definir herramientas personalizadas
2. Asignarlas a los agentes
3. Manejar las llamadas a herramientas
4. Procesar los resultados
"""

from typing import Dict, Any, List
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
import time
import json

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
client = OpenAI()


def calcular_estadisticas(numeros: List[float]) -> Dict[str, float]:
    """Calcula estadísticas básicas de una lista de números."""
    if not numeros:
        return {"promedio": 0, "minimo": 0, "maximo": 0, "suma": 0}
    return {
        "promedio": sum(numeros) / len(numeros),
        "minimo": min(numeros),
        "maximo": max(numeros),
        "suma": sum(numeros),
    }


def generar_grafico(datos: List[float], tipo: str) -> str:
    """Genera una representación ASCII de un gráfico."""
    if not datos:
        return "No hay datos para graficar"
    if tipo == "linea":
        return "📈 " + " ".join(str(d) for d in datos)
    elif tipo == "barras":
        return "📊 " + " ".join("█" * int(d) for d in datos)
    elif tipo == "dispersion":
        return "📉 " + " ".join("•" * int(d) for d in datos)
    else:
        return "Tipo de gráfico no soportado"


def crear_asistente(
    nombre: str, instrucciones: str, herramientas: list[Dict[str, Any]]
) -> Assistant:
    """Crea un asistente con herramientas personalizadas."""
    return client.beta.assistants.create(
        name=nombre,
        instructions=instrucciones,
        model="gpt-4o-mini",
        tools=herramientas,
    )


def crear_thread() -> Thread:
    """Crea un nuevo thread para la conversación."""
    return client.beta.threads.create()


def enviar_mensaje(thread_id: str, contenido: str) -> None:
    """Envía un mensaje al thread especificado."""
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=contenido
    )


def esperar_run(run, thread_id):
    """Espera a que el run termine y devuelve el run actualizado."""
    while run.status not in ["completed", "failed", "requires_action"]:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
    return run


def manejar_tool_calls(run, thread_id):
    """Procesa los tool calls solicitados por el asistente."""
    if not run.required_action or not hasattr(
        run.required_action, "submit_tool_outputs"
    ):
        return
    tool_outputs = []
    for tool_call in run.required_action.submit_tool_outputs.tool_calls:
        nombre = tool_call.function.name
        argumentos = json.loads(tool_call.function.arguments)
        if nombre == "calcular_estadisticas":
            resultado = calcular_estadisticas(argumentos["numeros"])
        elif nombre == "generar_grafico":
            resultado = generar_grafico(argumentos["datos"], argumentos["tipo"])
        else:
            resultado = f"Función desconocida: {nombre}"
        tool_outputs.append(
            {
                "tool_call_id": tool_call.id,
                "output": json.dumps(resultado, ensure_ascii=False),
            }
        )
    # Enviar resultados de las herramientas
    run = client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id, run_id=run.id, tool_outputs=tool_outputs
    )
    return run


def obtener_respuesta(thread_id: str, assistant_id: str) -> str:
    """Obtiene la respuesta del asistente para el último mensaje, manejando tool calls si es necesario."""
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )
    while True:
        run = esperar_run(run, thread_id)
        if run.status == "requires_action":
            run = manejar_tool_calls(run, thread_id)
            continue
        elif run.status == "completed":
            break
        elif run.status == "failed":
            return "El asistente falló al procesar la solicitud."
    # Obtener el último mensaje
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value


def main():
    # Definir herramientas personalizadas
    herramientas = [
        {
            "type": "function",
            "function": {
                "name": "calcular_estadisticas",
                "description": "Calcula estadísticas básicas de una lista de números",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numeros": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Lista de números para analizar",
                        }
                    },
                    "required": ["numeros"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "generar_grafico",
                "description": "Genera un gráfico de los datos proporcionados",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "datos": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Datos para graficar",
                        },
                        "tipo": {
                            "type": "string",
                            "enum": ["linea", "barras", "dispersion"],
                            "description": "Tipo de gráfico a generar",
                        },
                    },
                    "required": ["datos", "tipo"],
                },
            },
        },
    ]

    # Crear asistente analista
    asistente_analista = crear_asistente(
        "Analista de Datos",
        "Eres un analista de datos experto. Puedes calcular estadísticas "
        "y generar gráficos de los datos proporcionados.",
        herramientas,
    )

    # Crear thread
    thread = crear_thread()

    # Enviar mensaje con datos
    enviar_mensaje(thread.id, "Analiza estos datos: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")

    # Obtener análisis
    analisis = obtener_respuesta(thread.id, asistente_analista.id)
    print("\nAnálisis de datos:")
    print(analisis)

    # Enviar solicitud de gráfico
    enviar_mensaje(thread.id, "Genera un gráfico de línea con los mismos datos")

    # Obtener respuesta del gráfico
    respuesta_grafico = obtener_respuesta(thread.id, asistente_analista.id)
    print("\nRespuesta sobre el gráfico:")
    print(respuesta_grafico)


if __name__ == "__main__":
    main()
