"""
Script para validar que el entorno de desarrollo está configurado correctamente.
"""

import sys
import platform
from typing import List, Tuple


def check_python_version() -> Tuple[bool, str]:
    """Verifica la versión de Python."""
    version = platform.python_version()
    required_version = (3, 8)
    current_version = tuple(map(int, version.split(".")))

    if current_version >= required_version:
        return True, f"✅ Python {version} (cumple con el requisito mínimo de 3.8)"
    return False, f"❌ Python {version} (se requiere 3.8 o superior)"


def check_dependencies() -> List[Tuple[bool, str]]:
    """Verifica que las dependencias principales estén instaladas."""
    results = []

    try:
        import requests

        results.append((True, f"✅ requests {requests.__version__}"))
    except ImportError:
        results.append((False, "❌ requests no está instalado"))

    try:
        import pkg_resources

        dotenv_version = pkg_resources.get_distribution("python-dotenv").version
        results.append((True, f"✅ python-dotenv {dotenv_version}"))
    except (ImportError, pkg_resources.DistributionNotFound):
        results.append((False, "❌ python-dotenv no está instalado"))

    try:
        import pytest

        results.append((True, f"✅ pytest {pytest.__version__}"))
    except ImportError:
        results.append((False, "❌ pytest no está instalado"))

    try:
        import black

        results.append((True, f"✅ black {black.__version__}"))
    except ImportError:
        results.append((False, "❌ black no está instalado"))

    try:
        import flake8

        results.append((True, f"✅ flake8 {flake8.__version__}"))
    except ImportError:
        results.append((False, "❌ flake8 no está instalado"))

    return results


def main():
    """Función principal que ejecuta todas las validaciones."""
    print("\n=== Validación del Entorno de Desarrollo ===\n")

    # Verificar versión de Python
    python_ok, python_msg = check_python_version()
    print(python_msg)

    # Verificar dependencias
    print("\nVerificando dependencias:")
    deps_results = check_dependencies()
    for ok, msg in deps_results:
        print(msg)

    # Resumen
    all_ok = python_ok and all(ok for ok, _ in deps_results)
    print("\n=== Resumen ===")
    if all_ok:
        print(
            "🎉 ¡Todo está configurado correctamente! El entorno está "
            "listo para desarrollar."
        )
    else:
        print(
            "⚠️ Se encontraron algunos problemas. Por favor, revisa los "
            "mensajes anteriores."
        )

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
