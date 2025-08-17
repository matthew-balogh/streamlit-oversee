import streamlit as st

st.write("Formula for calculating the Manhattan-distance:")
st.code("""
p1 = [2, 4, 5]
p2 = [5, 1, 9]

distance = sum(abs(a - b) for a, b in zip(p1, p2))
""", language="python")

p1 = [2, 4, 5]
p2 = [5, 1, 9]

distance = sum(abs(a - b) for a, b in zip(p1, p2))

st.write(f"The distance is: {distance}")