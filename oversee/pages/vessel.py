import streamlit as st
import os

from oversee.utilities.helpers import get_active_vessel_label_html
from oversee.utilities.paths import VESSEL_DIRURL

DESCRIPTION_FILEPATH = f"{VESSEL_DIRURL}/description.md"

st.header(":material/sailing: Vessel")
st.html(get_active_vessel_label_html(id="vessel-page-vessel-label"))

if os.path.exists(DESCRIPTION_FILEPATH):
    with open(DESCRIPTION_FILEPATH, "r") as f:
        content = f.read()
        f.close()
    st.markdown(content)