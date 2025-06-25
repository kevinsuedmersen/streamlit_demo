import streamlit as st

from src.page_logic._base_page import BasePage


class ByeWorldPage(BasePage):
    def display(self) -> None:
        st.write("Goodbye World!")
