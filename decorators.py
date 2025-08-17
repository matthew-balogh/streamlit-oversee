import streamlit as st

from functools import wraps
from helpers import is_demo_mode

def skip_if_demo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_demo_mode():
            st.toast(f"Interrupted function call due to demo mode")
            return None
        return func(*args, **kwargs)
    return wrapper