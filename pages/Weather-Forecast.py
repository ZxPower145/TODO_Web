import streamlit as st
import plotly.express as px

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
    text = f"{option} for the next day in {place}: "
else:
    text = f"{option} for the next {days} days in {place}: "
st.subheader(text)


def get_data(days_lc):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temp = [10, 11, 15]
    temp = [days_lc * i for i in temp]
    return dates, temp


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date",
                                   "y": "Temperature(C)"})
st.plotly_chart(figure)
