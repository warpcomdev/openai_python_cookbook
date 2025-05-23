"""
Ejemplo de flujo de trabajo colaborativo entre múltiples agentes.

Este script demuestra cómo varios agentes pueden trabajar juntos en una tarea compleja,
donde cada agente tiene un rol específico y contribuye con sus capacidades únicas.

Los agentes pueden:
- Comunicarse entre sí a través de threads compartidos
- Pasarse el control de manera fluida
- Mantener el contexto de la conversación
- Usar herramientas especializadas
- Coordinar sus acciones para lograr un objetivo común

El flujo de trabajo incluye:
1. Asignación de roles y responsabilidades
2. Establecimiento de protocolos de comunicación
3. Coordinación de acciones y transferencias
4. Manejo de estados y contextos compartidos
5. Resolución colaborativa de tareas complejas
"""

from typing import Dict, Any
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
client = OpenAI()


def crear_asistente(
    nombre: str, instrucciones: str, herramientas: list[Dict[str, Any]] = None
) -> Assistant:
    """Crea un asistente con instrucciones y herramientas opcionales."""
    params = {
        "name": nombre,
        "instructions": instrucciones,
        "model": "gpt-4o-mini",
    }
    if herramientas:
        params["tools"] = herramientas
    return client.beta.assistants.create(**params)


def crear_thread() -> Thread:
    """Crea un nuevo thread para la conversación."""
    return client.beta.threads.create()


def enviar_mensaje(thread_id: str, contenido: str) -> None:
    """Envía un mensaje al thread especificado."""
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=contenido
    )


def obtener_respuesta(thread_id: str, assistant_id: str) -> str:
    """Obtiene la respuesta del asistente para el último mensaje."""
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run.status == "completed":
            break

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value


def main():
    # Crear asistentes especializados
    asistente_investigador = crear_asistente(
        "Investigador",
        "Eres un investigador experto. Tu tarea es analizar "
        "información y extraer datos relevantes.",
    )

    asistente_analista = crear_asistente(
        "Analista",
        "Eres un analista de datos. Tu tarea es interpretar "
        "datos y generar insights.",
    )

    asistente_reportero = crear_asistente(
        "Reportero",
        "Eres un reportero experto. Tu tarea es crear "
        "informes claros y concisos basados en análisis.",
    )

    # Crear thread
    thread = crear_thread()

    # Fase 1: Investigación
    enviar_mensaje(
        thread.id, "Investiga sobre el impacto de la IA en el mercado laboral"
    )
    investigacion = obtener_respuesta(thread.id, asistente_investigador.id)
    print("\nFase 1 - Investigación:")
    print(investigacion)

    # Fase 2: Análisis
    enviar_mensaje(
        thread.id, f"Analiza esta información y extrae insights clave: {investigacion}"
    )
    analisis = obtener_respuesta(thread.id, asistente_analista.id)
    print("\nFase 2 - Análisis:")
    print(analisis)

    # Fase 3: Reporte
    enviar_mensaje(
        thread.id, f"Crea un reporte ejecutivo basado en este análisis: {analisis}"
    )
    reporte = obtener_respuesta(thread.id, asistente_reportero.id)
    print("\nFase 3 - Reporte Final:")
    print(reporte)

    # --- Ejemplo adicional: Agente de triaje ---
    print("\n--- Ejemplo adicional: Triaje automático ---")

    # Crear agente de triaje
    asistente_triaje = crear_asistente(
        "Triaje",
        "Eres un agente de triaje. Tu tarea es decidir cuál de los siguientes agentes debe encargarse de la consulta: 'investigador', 'analista' o 'reportero'. Responde solo con el nombre del agente más adecuado para la tarea: investigador, analista o reportero. No expliques tu decisión.",
    )

    # Consulta de ejemplo
    consulta_usuario = "Por favor, analiza el impacto de la automatización en el empleo y genera un informe ejecutivo."
    print(f"\nConsulta de usuario: {consulta_usuario}")

    # El agente de triaje decide a quién derivar la consulta
    enviar_mensaje(
        thread.id, f"¿Qué agente debe encargarse de esta consulta? {consulta_usuario}"
    )
    decision = obtener_respuesta(thread.id, asistente_triaje.id).strip().lower()
    print(f"Agente de triaje sugiere: {decision}")

    # Diccionario para mapear nombres a asistentes
    agentes = {
        "investigador": asistente_investigador,
        "analista": asistente_analista,
        "reportero": asistente_reportero,
    }

    # Ejecutar la consulta con el agente sugerido
    if decision in agentes:
        enviar_mensaje(thread.id, consulta_usuario)
        respuesta = obtener_respuesta(thread.id, agentes[decision].id)
        print(f"\nRespuesta del agente '{decision}':")
        print(respuesta)
    else:
        print("El agente de triaje no dio una respuesta válida.")


if __name__ == "__main__":
    main()
