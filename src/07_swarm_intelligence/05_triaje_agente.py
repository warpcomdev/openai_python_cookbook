"""
Ejemplo de agente de triaje para soporte técnico de TI.

Este script crea cuatro agentes:
- Triaje: decide a qué agente derivar la consulta
- Hardware: resuelve problemas de dispositivos físicos, periféricos, etc.
- Software: resuelve problemas de programas, sistemas operativos, aplicaciones
- Redes: resuelve problemas de conectividad, internet, routers, etc.

El usuario introduce una consulta, el agente de triaje decide el área adecuada,
y el script ejecuta la consulta con ese agente, mostrando la respuesta.
"""

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
client = OpenAI()


def crear_asistente(nombre: str, instrucciones: str) -> Assistant:
    """Crea un asistente con instrucciones."""
    return client.beta.assistants.create(
        name=nombre,
        instructions=instrucciones,
        model="gpt-4o-mini",
    )


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
    # Crear agentes
    asistente_hardware = crear_asistente(
        "Hardware",
        "Eres un especialista en hardware de TI. Resuelves problemas "
        "relacionados con dispositivos físicos, componentes, periféricos, "
        "impresoras, discos duros, etc.",
    )
    asistente_software = crear_asistente(
        "Software",
        "Eres un especialista en software de TI. Resuelves problemas "
        "relacionados con programas, sistemas operativos, aplicaciones, "
        "instalación y configuración de software, etc.",
    )
    asistente_redes = crear_asistente(
        "Redes",
        "Eres un especialista en redes de TI. Resuelves problemas "
        "relacionados con conectividad, internet, routers, Wi-Fi, cableado, etc.",
    )
    asistente_triaje = crear_asistente(
        "Triaje",
        "Eres un agente de triaje de soporte técnico. Tu tarea es decidir "
        "cuál de los siguientes agentes debe encargarse de la consulta: "
        "'hardware', 'software' o 'redes'. Responde solo con el nombre del "
        "agente más adecuado para la tarea: hardware, software o redes. "
        "No expliques tu decisión.",
    )

    # Crear thread
    thread = crear_thread()

    print("\nEscribe tu consulta de soporte técnico " "(o 'salir' para terminar):")
    while True:
        consulta_usuario = input("\nConsulta: ").strip()
        if consulta_usuario.lower() == "salir":
            print("Saliendo del sistema de triaje de soporte técnico.")
            break
        if not consulta_usuario:
            print("Por favor, introduce una consulta válida.")
            continue
        print(f"Consulta de usuario: {consulta_usuario}")

        # El agente de triaje decide a quién derivar la consulta
        enviar_mensaje(
            thread.id,
            ("¿Qué agente debe encargarse de esta consulta? " f"{consulta_usuario}"),
        )
        decision = obtener_respuesta(thread.id, asistente_triaje.id).strip().lower()
        print(f"Agente de triaje sugiere: {decision}")

        # Diccionario para mapear nombres a asistentes
        agentes = {
            "hardware": asistente_hardware,
            "software": asistente_software,
            "redes": asistente_redes,
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
