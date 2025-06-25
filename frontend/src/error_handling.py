"""Error handling decorators."""
import logging
import traceback
from typing import Callable

import requests.exceptions
import streamlit as st

logger = logging.getLogger(__name__)


def handle_any_exception(func: Callable) -> Callable:
    """Decorator handling any possible exception. Logging complete error message to console and displaying minimum
    error info to the user.

    Parameters
    ----------
    func: Callable
        Function to decorate.

    Returns
    -------
    Callable
    """
    def _wrapper(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.error(f"The following unexpected error occurred: {repr(error)}")
            traceback.print_exc()
            st.markdown(
                f"The following error occurred while processing your request:\n`{repr(error)}`.\n\n"
                "Please contact an administrator and show him/her this error messsage."
            )

    return _wrapper


def handle_invalid_request(request_func: Callable) -> Callable:
    """Decorator handling potentially invalid requests to the clerky api.

    Parameters
    ----------
    request_func: Callable
        Function executing the raw request to the clerky backend.

    Returns
    -------
    Callable
    """
    def _wrapper(*args, **kwargs) -> requests.Response:
        try:
            response = request_func(*args, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP error occurred: {err}, Status code: {err.response.status_code}, Reason: {err.response.reason}")
            raise err

    return _wrapper
