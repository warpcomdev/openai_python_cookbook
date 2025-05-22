"""
Pruebas unitarias para el ejemplo básico.
"""
import os
from unittest.mock import patch

import pytest
from src.example import get_completion


def test_get_completion_missing_api_key():
    """Prueba que se lance una excepción cuando no hay API key."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="OPENAI_API_KEY no encontrada"):
            get_completion("test prompt")


@patch("requests.post")
def test_get_completion_success(mock_post):
    """Prueba una llamada exitosa a la API."""
    # Configurar el mock
    mock_response = {"choices": [{"message": {"content": "Test response"}}]}
    mock_post.return_value.json.return_value = mock_response

    # Configurar la API key
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        response = get_completion("test prompt")

        # Verificar que se llamó a la API con los parámetros correctos
        mock_post.assert_called_once()
        call_args = mock_post.call_args[1]
        assert call_args["headers"]["Authorization"] == "Bearer test-key"
        assert call_args["json"]["model"] == "gpt-3.5-turbo"
        assert call_args["json"]["messages"][0]["content"] == "test prompt"

        # Verificar la respuesta
        assert response == mock_response
