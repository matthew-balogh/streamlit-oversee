import streamlit as st
import os
import json

STORAGE_DIRURL = "storage"
VESSEL_DIRURL = f"{STORAGE_DIRURL}/vessel"

DEMO_MODE_MESSAGE = "Not available in demo mode!"

def is_demo_mode() -> bool:
    if os.path.exists(".streamlit/secrets.toml"):
        return (st.secrets.get("demo_mode", False) == True)
    else:
        return False

def get_demo_banner_html():
    return """
<style>
    #oversee-demo-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        z-index: 10;

        padding: .75rem 1.5rem;
        background: rgba(255, 90, 94, .9);
        border-radius: 0 1.75rem 0 0;

        color: white;
        text-decoration: none;
    }

    #oversee-demo-banner:hover {
        cursor: pointer;
    }
</style>

<a href="/" target="_self" id="oversee-demo-banner"><b>Demo mode:</b> Visit <b>Help</b> or <u>click here</u> to get started.</a>
"""

def get_demo_mode_toast():
    return st.toast(DEMO_MODE_MESSAGE, icon=":material/no_sim:")

PRIMARY_COLOR = st.get_option('theme.primaryColor')

def get_vessel_title():
    DETAILS_FILEPATH = f"{VESSEL_DIRURL}/details.json"

    vessel_title = st.session_state.get("vessel-title", None)

    if (vessel_title is None) and os.path.exists(DETAILS_FILEPATH):
        with open(DETAILS_FILEPATH, "r") as f:
            content = json.load(f)
            vessel_title = content["title"]
            f.close()
    else:
        print("Cannot retrieve vessel title")
        st.toast("Cannot retrieve vessel title")

    return vessel_title

def get_active_vessel_label_html(id, styling=""):
    return f"""
<style>
    .vessel-label {{
        cursor: default;
        background: {PRIMARY_COLOR};
        color: white;

        font-size: 16px;
        padding: .5rem .75rem;
        border-radius: .6rem;
        width: max-content;
    }}

    .vessel-label#{id} {{
        {styling}
    }}
</style>

<div id={id} class="vessel-label">
{get_vessel_title()}
</div>
"""