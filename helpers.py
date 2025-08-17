import streamlit as st
import os

def is_demo_mode() -> bool:
    return (st.secrets.get("demo_mode", False) == True)