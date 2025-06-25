import streamlit as st

from src.pages._base_page import BasePage
from src.settings import Settings
from src.clients import BaseAPIClient
from src.error_handling import handle_any_exception


class LoginPage(BasePage):
    def __init__(self, settings: Settings, api_client: BaseAPIClient) -> None:
        super().__init__(settings)
        self._api_client = api_client
    
    @handle_any_exception
    def display(self) -> None:
        with st.sidebar:
            api_token = self._api_client._get_api_token()

        successful_connection = self._api_client.test_connection()
        if successful_connection:
            st.write(
                f"Welcome {api_token.username}! You successfully logged in. "
                f"You have {api_token.lifetime_end - api_token.lifetime_start} seconds until you need to login again."
            )
        else:
            st.error(
                "Connecting to the backend api failed."
            )
        
        st.write("This is your Bearer token:")
        st.code(api_token.value)
