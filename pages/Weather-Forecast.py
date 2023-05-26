import streamlit as st
import plotly.express as px
from files import weather_backend

st.set_page_config(layout="wide",
                   page_title="Weather Forecast",
                   page_icon="🌤️", )

st.title("Weather forcast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of the days for which you want to see the forecast ")
option = st.selectbox(
    "Select how you wish to view the data: ",
    ("Temperature", "Sky")
)

if days == 1:
    text = f"{option} for the next day in {place.capitalize()}: "
else:
    text = f"{option} for the next {days} days in {place.capitalize()}: "

if place:
    try:
        filtered_data, location = weather_backend.get_data(place, days)
        if place in location["name"]:
            a = st.subheader(text)
        else:
            a = ""
        if option == "Temperature":
            temp = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date",
                                                      "y": "Temperature(C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "files/sky/clear.png",
                      "Clouds": "files/sky/cloud.png",
                      "Rain": "files/sky/rain.png",
                      "Snow": "files/sky/snow.png"}
            st.image([images[condition] for condition in sky_condition], width=150)
    except KeyError:
        a = None
        st.warning("Please provide an existing place!")
