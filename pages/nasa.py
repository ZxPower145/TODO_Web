import streamlit as st
import requests

api_key = "L9nav9iTG8rpUOMxWPjZmp73iyAww8oYimwbyoQ9"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()
date = content["date"]
description = content["explanation"]
image_url = content["url"]
title = content["title"]

st.set_page_config(layout="wide",
                   page_icon="🌍",
                   page_title="Nasa picture of the day")

col1, col2, col3 = st.columns(3)

with col1:
    st.header(date)

with col2:
    st.header(title)
    st.image(image_url, width=600)
    st.subheader(description)

with col3:
    st.write(' ')
