import streamlit as st
from streamlit_msal import Msal

from src.init_app import init_app


if __name__ == "__main__":
    init_app()
    st.session_state.login_page.display()
