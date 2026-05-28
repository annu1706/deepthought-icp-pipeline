import streamlit as st
import pandas as pd

st.title("DeepThought ICP Dashboard")

df = pd.read_csv("output/final_scores.csv")

st.metric("Total Companies", len(df))

st.dataframe(df)