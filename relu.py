import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.markdown("### Mathematical Formula")
st.latex(r"f(x) = \max(0, x)")

x = np.linspace(-10, 10, 100)
relu = np.maximum(0, x)

st.markdown("### Visualization")
plt.figure()
plt.plot(x, relu)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("ReLU Function")

st.pyplot(plt)

