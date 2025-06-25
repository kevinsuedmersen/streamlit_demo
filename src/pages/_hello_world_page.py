import streamlit as st

from src.pages._base_page import BasePage
from src.settings import Settings
from src.clients import BackendAPIClient
from src.error_handling import handle_any_exception


class HelloWorldPage(BasePage):
    def __init__(self, settings: Settings, backend_api_client: BackendAPIClient) -> None:
        super().__init__(settings)
        self._backend_api_client = backend_api_client

    @handle_any_exception
    def display(self) -> None:
        if st.session_state.is_successful_connection is None:
            st.write("Connection to the backend hasn't been tested yet.")

            if st.button("Test Connection"):
                # Test connection and cache the result
                st.session_state.is_successful_connection = self._backend_api_client.test_connection()

                if st.session_state.is_successful_connection:
                    st.write(f"Connecting to the backend api worked!")
                else:
                    st.error("Connecting to the backend api failed.")
