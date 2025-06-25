import logging

import streamlit as st

from src.settings import get_settings
from src.pages import LoginPage
from src.clients import BackendAPIClient
from src.api_tokens import AzureAPIToken

logger = logging.getLogger(__name__)


def init_app() -> None:
    if ("initialized_app" not in st.session_state) or (not st.session_state.initialized_app):
        with st.spinner("Initializing app..."):
            logger.debug("Initializing app")
            settings = get_settings()

            # Instantiate objects
            api_client = BackendAPIClient(
                settings=settings,
                api_token_cls=AzureAPIToken,
            )
            login_page = LoginPage(
                settings=settings,
                api_client=api_client,
            )

            # Update the session state
            st.session_state.update({
                "settings": settings,
                "login_page": login_page,
            })
            st.session_state.initialized_app = True
            logger.debug("App has been initialized")
