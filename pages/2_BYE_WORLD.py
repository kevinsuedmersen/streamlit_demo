import streamlit as st

from src.init_app import init_app


if __name__ == "__main__":
    init_app()
    st.session_state.bye_world_page.display()
