import streamlit as st

def is_demo_mode() -> bool:
    return (st.secrets.get("demo_mode", False) == True)

def get_demo_banner_html():
    return """
<style>
    #oversee-demo-banner {
        position: fixed;
        bottom: 0;
        left: 0;

        padding: .5rem 1.5rem;
        background: rgba(255, 90, 94, .9);
        border-radius: 0 1.75rem 0 0;

        color: white;
        text-decoration: none;
    }

    #oversee-demo-banner:hover {
        cursor: pointer;
    }
</style>

<a href="/help" target="_self" id="oversee-demo-banner"><b>Demo mode:</b> Visit <u>Help</u> for getting started</a>
"""