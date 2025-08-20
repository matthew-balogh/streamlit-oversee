import streamlit as st

st.set_page_config(
    page_title="Come Aboard!",
    page_icon="assets/logo.png",
    layout="wide"
)

intro_html = """
<style>
    #landing-intro-text {
        display: block;
        margin-top: 2rem;
        color: #8195ac;
        font-size: 1.6rem;

        .highlighted {
            color: #416793;
        }
    }
</style>

<span id="landing-intro-text">
    <span class="highlighted">Oversee</span> your <span class="highlighted">data experiments</span> while in the harbor,<br>stay focused and organized overseas, and share clear findings on return.
</span>
"""

fetch_html = """
<style>
    #landing-fetch-container {
        display: flex;
        flex-direction: column;
        margin-top: .5rem;
        color: #8195ac;

        .highlighted {
            color: #416793;
            font-weight: 500;
        }

        .highlighted-2 {
            color: #b098c4;
            font-weight: 400;
        }

        .fetch-caption {
            color: #C6CAD0 !important;
            font-size: 2rem;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
        }

        .fetch-block {
            font-size: 1.5rem;

            span:not(:first-child) {
                display: block;
                margin-left: 4rem;
            }
        }
    }
</style>

<div id="landing-fetch-container">
    <span class="fetch-caption">Fetch your Vessel...</span>
    <div class="fetch-block">
        <span>$  clone <span class="highlighted">streamlit-oversee</span></span>
        <span>as <span class="highlighted">oversee-my-data-science-project</span></span>
        <span class="highlighted-2">--save-to-my-github</span>
    </div>
    <div class="fetch-block">
        <span>$  run <span class="highlighted">oversee-my-data-science-project</span></span></span>
    </div>
    <div class="fetch-block">
        <span class="highlighted-2">🎈🎉  App started at <u>http://localhost:8501</u></span>
    </div>
    <span class="fetch-caption">Start Overseeing your work...</span>
</div>
"""

col1, col2 = st.columns([1, 10])

with col2:
    with st.container(horizontal=True, horizontal_alignment="left"):
        st.image("assets/logo_image_full_wo_padding.png")

    st.markdown(intro_html, width=600, unsafe_allow_html=True)
    st.markdown(fetch_html, width=600, unsafe_allow_html=True)

    st.link_button("Get started here", type="primary", icon=":material/sailing:", url="/help")

st.image("assets/waves_background.png", use_container_width=True)