import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/20.png")

with col2:
    st.title("Costin Bogdan")
    content = """
    Hi, I am Bogdan! I am a Python programmer, 
    I have close to 2 months experience with this language.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I developed, if you like my work feel
free to contact me :
"""
st.write(content2)

col3, colempty, col4 = st.columns([1.5, 0.3, 1.5])

data = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.info(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")