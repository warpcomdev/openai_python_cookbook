"""
Ejemplo básico de creación y uso de agentes con el Agents SDK.

Este script demuestra cómo crear agentes simples que pueden interactuar entre sí para realizar tareas colaborativas.
Los agentes son asistentes especializados que pueden:

- Tener roles y personalidades específicas
- Mantener conversaciones a través de threads
- Usar herramientas y funciones personalizadas
- Transferir el control entre ellos
- Mantener el contexto de la conversación

En este ejemplo crearemos agentes para generar y traducir haikus, mostrando:
- Creación de asistentes con diferentes roles
- Manejo de threads de conversación
- Envío y recepción de mensajes
- Coordinación entre agentes
"""

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
client = OpenAI()

# Temas disponibles para los haikus
TEMAS = [
    "primavera",
    "otoño",
    "invierno",
    "verano",
    "luna",
    "mar",
    "montaña",
    "flores",
    "amor",
    "soledad",
]

# Idiomas disponibles para traducción
IDIOMAS = {"1": "inglés", "2": "francés", "3": "italiano"}


def crear_asistente(nombre: str, instrucciones: str) -> Assistant:
    """Crea un asistente con el nombre y las instrucciones especificadas."""
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
    # Crear run
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )

    # Esperar a que el run termine
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run.status == "completed":
            break

    # Obtener el último mensaje
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value


def mostrar_menu_temas():
    """Muestra el menú de temas disponibles."""
    print("\nTemas disponibles para el haiku:")
    for i, tema in enumerate(TEMAS, 1):
        print(f"{i}. {tema.capitalize()}")
    while True:
        try:
            eleccion = int(input("\nElige un número de tema (1-10): "))
            if 1 <= eleccion <= len(TEMAS):
                return TEMAS[eleccion - 1]
            print("Por favor, elige un número válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


def mostrar_menu_idiomas():
    """Muestra el menú de idiomas disponibles."""
    print("\nIdiomas disponibles para traducción:")
    for codigo, idioma in IDIOMAS.items():
        print(f"{codigo}. {idioma.capitalize()}")
    while True:
        eleccion = input("\nElige los idiomas (ej: 1,2,3): ")
        idiomas_elegidos = []
        for codigo in eleccion.split(","):
            codigo = codigo.strip()
            if codigo in IDIOMAS:
                idiomas_elegidos.append(IDIOMAS[codigo])
        if idiomas_elegidos:
            return idiomas_elegidos
        print("Por favor, elige al menos un idioma válido.")


def preguntar_continuar():
    """Pregunta al usuario si desea crear otro haiku."""
    while True:
        respuesta = input("\n¿Deseas crear otro haiku? (s/n): ").lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print("Por favor, responde 's' para sí o 'n' para no.")


def crear_haiku_y_traducir(thread, asistente_poeta, asistente_traductor):
    """Crea un haiku y lo traduce a los idiomas seleccionados."""
    # Seleccionar tema
    tema = mostrar_menu_temas()
    print(f"\nHas elegido el tema: {tema.capitalize()}")

    # Enviar mensaje inicial
    enviar_mensaje(thread.id, f"Por favor, escribe un haiku sobre {tema}.")

    # Obtener respuesta del poeta
    haiku = obtener_respuesta(thread.id, asistente_poeta.id)
    print("\nHaiku original:")
    print(haiku)

    # Seleccionar idiomas para traducción
    idiomas = mostrar_menu_idiomas()
    print(
        f"\nTraduciendo a: " f"{', '.join(idioma.capitalize() for idioma in idiomas)}"
    )

    # Traducir a cada idioma seleccionado
    for idioma in idiomas:
        enviar_mensaje(thread.id, f"Por favor, traduce este haiku al {idioma}: {haiku}")
        traduccion = obtener_respuesta(thread.id, asistente_traductor.id)
        print(f"\nTraducción al {idioma.capitalize()}:")
        print(traduccion)


def main():
    # Crear asistentes
    asistente_poeta = crear_asistente(
        "Poeta",
        "Eres un poeta que solo responde en forma de haiku. "
        "Un haiku es un poema japonés de tres versos con 5-7-5 sílabas.",
    )

    asistente_traductor = crear_asistente(
        "Traductor",
        "Eres un traductor experto. Tu tarea es traducir los haikus "
        "manteniendo el formato y el significado.",
    )

    # Crear thread
    thread = crear_thread()

    print("¡Bienvenido al Generador de Haikus!")
    print("==================================")

    while True:
        crear_haiku_y_traducir(thread, asistente_poeta, asistente_traductor)

        if not preguntar_continuar():
            print("\n¡Gracias por usar el Generador de Haikus!")
            break


if __name__ == "__main__":
    main()
