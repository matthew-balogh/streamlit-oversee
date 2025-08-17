import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columns = ["col %d" % i for i in range(5)]

df = pd.DataFrame(np.random.default_rng(0).standard_normal((50, 5)), columns=columns)

st.write("Given the following dataset:")
st.dataframe(df)

st.write("Standardize it:")

X = df.values
means = np.mean(X, axis=0)
stds = np.std(X, axis=0)
X_stand = (X - means) / stds
df_dtand = pd.DataFrame(X_stand, columns=df.columns)

st.dataframe(df_dtand)

st.write("Comparison of ranges:")

fig, axes = plt.subplots(1, 2, figsize=(6, 3), sharex=True, sharey=True)
plt.tight_layout()

ax = axes[0]
ax.boxplot(df, vert=False)
ax.set_title("Original variables")

ax = axes[1]
ax.boxplot(df_dtand, vert=False)
ax.set_title("Standardized variables")

for ax in axes:
    ax.set_yticks(range(1, len(columns) + 1), columns)

st.pyplot(fig, use_container_width=False)