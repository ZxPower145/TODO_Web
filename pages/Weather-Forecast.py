import streamlit as st
import pandas as pd

st.set_page_config(layout="wide",
                   page_title="Weather Forecast",
                   page_icon="🌤️",)

st.title("Weather forcast for the next days")
place = st.text_input("Place: ")
slider = st.slider("Forecast Days", min_value=1, max_value=5,
                   help="Select the number of the days for which you want to see the forecast ")
option = st.selectbox(
    "Select how you wish to view the data: ",
    ("Temperature", "Sky")
)

if slider == 1:
    text = f"{option} for the next day in {place}: "
else:
    text = f"{option} for the next {slider} days in {place}: "

st.subheader(text)
