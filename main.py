import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)
col1.image("img/samsung-solve.png", width=100)
col2.title('Solve for Tomorrow Dashboard')

st.file_uploader("", type=None)
