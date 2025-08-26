import streamlit as st
import os

from oversee.utilities.helpers import get_active_vessel_label_html

STORAGE_DIRURL = "storage"
VESSEL_DIRURL = f"{STORAGE_DIRURL}/vessel"

DESCRIPTION_FILENAME = "description.md"
DESCRIPTION_FILEPATH = f"{VESSEL_DIRURL}/{DESCRIPTION_FILENAME}"

st.header(":material/sailing: Vessel")
st.html(get_active_vessel_label_html(id="vessel-page-vessel-label"))

if os.path.exists(DESCRIPTION_FILEPATH):
    with open(DESCRIPTION_FILEPATH, "r") as f:
        content = f.read()
        f.close()
    st.markdown(content)