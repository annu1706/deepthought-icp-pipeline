import streamlit as st
import pandas as pd

st.title("DeepThought ICP Dashboard")

df = pd.read_csv("output/final_scores.csv")

st.dataframe(df)

st.write("Total Companies:", len(df))