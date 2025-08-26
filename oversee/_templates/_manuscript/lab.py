import streamlit as st

template_md = """
To make changes in your manuscript, please visit the `storage/manuscripts/<OVERSEE_MANUSCRIPT_ID_PLACEHOLDER>` folder.
You can always access the identifier of your manuscripts when hovering over their **:material/contract: Manuscript** label above.

Your newly opened manuscript has the following structure:

* **Cabin Laboratory**: Experiment with your code and display only what's important.
    > To modify the content of your isolated laboratory, edit the `lab.py` file under the manuscript folder. You can always create separate notebook files to experiment in your local environment, but only the outputs of `lab.py` will be displayed here.
We recommend to use [Streamlit elements](https://docs.streamlit.io/develop/api-reference) for your writing and outputs.

* **Journal**: Take notes and jot down your thoughts.
    > To modify the content of your journal, edit the `notes.md` file under the manuscript folder.

* **Results & Future Directions**: State your findings and your next moves.
    > To state a result, edit the `results.md` file and set `"research_result"` to `true` in the `details.json` file under the manuscript folder.
    
    > To state a future direction, edit the `future_directions.md` file and set `"future_directions"` to `true` in the `details.json` file under the manuscript folder.
"""

st.markdown(template_md)
st.container(border=False, height=2)

st.write("In the app, you will see the following indicators to help distinguish manuscripts from each other:")
with st.container(horizontal=True, vertical_alignment="center"):
    st.button("", key="help:indicator:research_results", icon=":material/lab_panel:", type="tertiary", disabled=True)
    st.write("This icon indicates that research results have been obtained for the manuscript.")
with st.container(horizontal=True, vertical_alignment="center"):
    st.button("", key="help:indicator:future_directions", icon=":material/arrow_split:", type="tertiary", disabled=True)
    st.write("This icon indicates that future directions have been stated for the manuscript.")
st.container(border=False, height=1)

st.info("This content was copied from a template. You can safely remove and edit the entire content of the mentioned files under the manuscript folder.", icon=":material/info:")