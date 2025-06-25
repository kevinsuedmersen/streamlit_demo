import logging
import requests

from src.error_handling import handle_invalid_request
from src.settings import Settings

logger = logging.getLogger(__name__)


class BackendAPIClient:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._backend_api_token = None

    def test_connection(self) -> bool:
        logger.debug(f"Sending a test request to the backend url '{self._settings.backend_api_url}'")
        response = self._test_connection()
        if response.status_code == 200:
            logger.info("Test request to the backend successful.")
            return True
        else:
            logger.error("Test request to the backend was not successful.")
            return False

    def _get_api_token(self) -> str:
        if self._backend_api_token is None:
            logger.debug("Generating new api token.")
            self._backend_api_token = "abc123"
            return self._backend_api_token
        else:
            logger.debug("Retrieving api token from cache.")
            return self._backend_api_token

    def _get_headers(self) -> dict:
        token = self._get_api_token()
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

    @handle_invalid_request
    def _test_connection(self) -> requests.Response:
        response = requests.get(
            url=self._settings.backend_api_url,
            headers=self._get_headers()
        )
        return response
