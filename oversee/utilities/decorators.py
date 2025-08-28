import streamlit as st
import uuid

from pathlib import Path
from functools import wraps

from oversee.utilities.helpers import is_demo_mode
from oversee.utilities.paths import STORAGE_DIRURL, DIVE_FILENAME, DIVES_FILENAME

def skip_if_demo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_demo_mode():
            st.toast(f"Interrupted function call due to demo mode")
            return None
        return func(*args, **kwargs)
    return wrapper

def with_dive_filepath():
    def decorator(func):
        @wraps(func)
        @with_demo_session_id()
        def wrapper(*args, demo_session_id: str, **kwargs):
            if demo_session_id is not None:
                parent = f"{STORAGE_DIRURL}/{demo_session_id}"
            else: parent=f"{STORAGE_DIRURL}"

            dive_filepath = Path(f"{parent}/{DIVE_FILENAME}")

            return func(dive_filepath=dive_filepath, *args, **kwargs)
        return wrapper
    return decorator

def with_manuscript_dives_filepath():
    def decorator(func):
        @wraps(func)
        @with_manuscript_folder()
        def wrapper(*args, manuscript_folder: Path, **kwargs):
            manuscript_dives_filepath = Path(f"{manuscript_folder}/{DIVES_FILENAME}")

            return func(manuscript_dives_filepath=manuscript_dives_filepath, *args, **kwargs)
        return wrapper
    return decorator

def with_new_manuscript_id():
    def decorator(func):
        @wraps(func)
        @with_demo_session_id()
        def wrapper(*args, demo_session_id: str, **kwargs):
            manuscript_id = str(uuid.uuid4())

            if demo_session_id is not None:
                manuscript_id = f"demo-{manuscript_id}"

            return func(*args, manuscript_id=manuscript_id, **kwargs)
        return wrapper
    return decorator

def with_manuscript_folder():
    def decorator(func):
        @wraps(func)
        @with_demo_session_id()
        def wrapper(*args, demo_session_id: str, manuscript_id: str, **kwargs):
            if manuscript_id is None:
                raise Exception("`manuscript_id` must be set for `@with_manuscript_folder")
            
            if manuscript_id.startswith("demo-"):
                parent = f"{STORAGE_DIRURL}/{demo_session_id}"
            else: parent=f"{STORAGE_DIRURL}"

            manuscript_folder = Path(f"{parent}/manuscripts/{manuscript_id}")

            return func(manuscript_folder=manuscript_folder, manuscript_id=manuscript_id, *args, **kwargs)
        return wrapper
    return decorator

def with_manuscript_parent_folders():
    def decorator(func):
        @wraps(func)
        @with_demo_session_id()
        def wrapper(*args, demo_session_id: str, **kwargs):
            parents = []

            if demo_session_id is not None:
                parents.append(f"{STORAGE_DIRURL}/{demo_session_id}")
                parents.append(STORAGE_DIRURL)
            else: parents.append(STORAGE_DIRURL)

            manuscript_parent_folders = list(map(lambda x: Path(f"{x}/manuscripts"), parents))

            return func(manuscript_parent_folders=manuscript_parent_folders, *args, **kwargs)
        return wrapper
    return decorator

def with_demo_session_id():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            demo_session_id = None

            if is_demo_mode():
                demo_session_id = st.session_state.get("demo_session_id", None)
                if demo_session_id is None:
                    raise Exception("Session id could not be found. Please reload the application.")

            return func(demo_session_id=demo_session_id, *args, **kwargs)
        return wrapper
    return decorator