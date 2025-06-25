"""Error handling decorators."""
import logging
import traceback
import requests

from typing import Callable
from unittest.mock import Mock

logger = logging.getLogger(__name__)


def handle_invalid_request(request_func: Callable) -> Callable:
    """Decorator handling potentially invalid requests to the backend api.

    Parameters
    ----------
    request_func: Callable
        Function executing the raw request to the backend backend.

    Returns
    -------
    Callable
    """
    def _wrapper(*args, **kwargs) -> requests.Response:
        try:
            response = request_func(*args, **kwargs)
            response.raise_for_status()
            return response
        except Exception as err:
            # Mock an internal server error
            logger.error(f"The following error occurred while processing a request: {err}")
            traceback.print_exc()
            mock_response = Mock()
            mock_response.status_code = 500
            mock_response.text = "Internal Server Error"
            mock_response.json.return_value = {"error": "Internal Server Error"}
            mock_response.ok = False
            return mock_response

    return _wrapper
