import streamlit as st

from functools import wraps
from oversee.utilities.helpers import is_demo_mode

def skip_if_demo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_demo_mode():
            st.toast(f"Interrupted function call due to demo mode")
            return None
        return func(*args, **kwargs)
    return wrapper

def fallback_to_session_storage_read_in_demo(session_key):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_demo_mode():
                st.session_state.setdefault(session_key, {})
                data = func()
                data.extend(list(st.session_state.get(session_key, {}).values()))
                return data
            else:
                return func()
        return wrapper
    return decorator

def fallback_to_session_storage_write_in_demo(session_parent_key, session_entry_key, entry):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_demo_mode():
                st.session_state[session_parent_key][session_entry_key] = entry
            else:
                return func(entry)
        return wrapper
    return decorator