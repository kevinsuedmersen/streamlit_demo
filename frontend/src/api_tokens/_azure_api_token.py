import time
from typing import Optional

import streamlit as st
from streamlit_msal import Msal
from pydantic import BaseModel, Field, computed_field

from src.settings import Settings
from src.api_tokens._base_api_token import BaseAPIToken


class AzureAPIToken(BaseAPIToken):
    @computed_field
    @property
    def is_expired(self) -> bool:
        if (self.lifetime_end - time.time()) <= self.lifetime_buffer:
            return True
        else:
            return False
        
    @classmethod
    def from_signed_in_user(cls, settings: Settings) -> "AzureAPIToken":
        auth_data = Msal.initialize_ui(
            client_id=settings.frontend_client_id,
            authority=settings.frontend_authority,
            scopes=[settings.backend_scope_name], 
        )
        if not auth_data:
            st.write("Please sign before using this application.")
            st.stop()
        account = auth_data["account"]
        lifetime_start = int(time.time())
        if ("idTokenClaims" in auth_data) and ("exp" in auth_data["idTokenClaims"]):
            lifetime_end = auth_data["idTokenClaims"]["exp"]
        else:
            lifetime_end = lifetime_start + settings.backend_api_max_token_lifetime 
        return cls(
            value=auth_data["accessToken"],
            username=account["username"],
            user_id=account["localAccountId"],
            lifetime_start=lifetime_start,
            lifetime_end=lifetime_end,
            max_lifetime=settings.backend_api_max_token_lifetime,
            lifetime_buffer=settings.backend_api_token_lifetime_buffer,
        )
        
   