import streamlit as st

st.subheader("Laboratory Notebook")
st.caption(f"Case id: {st.query_params['case_id']}")