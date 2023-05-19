import streamlit as st

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