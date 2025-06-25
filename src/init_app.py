import logging

import streamlit as st

from src.settings import get_settings
from src.page_logic import HelloWorldPage, ByeWorldPage
from src.clients import BackendAPIClient

logger = logging.getLogger(__name__)


def init_app() -> None:
    if ("initialized_app" not in st.session_state) or (not st.session_state.initialized_app):
        with st.spinner("Initializing app..."):
            logger.debug("Initializing app")
            settings = get_settings()

            # Instantiate objects
            backend_api_client = BackendAPIClient(settings)
            hello_world_page = HelloWorldPage(settings, backend_api_client)
            bye_world_page = ByeWorldPage(settings)

            # Update the session state
            st.session_state.update({
                "settings": settings,
                "hello_world_page": hello_world_page,
                "bye_world_page": bye_world_page,
                "is_successful_connection": None
            })
            st.session_state.initialized_app = True
            logger.debug("App has been initialized")
