import streamlit as st
import plotly.express as px
import pandas as pd

file = pd.read_csv("../files/happy.csv")

st.set_page_config(layout="wide", page_title="Happiness data API", page_icon="😁")
st.header("In search for happiness")
x_axis = st.selectbox("Select the data for the X-Axis: ",
                      ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-Axis: ",
                      ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")


def get_data():
    user_choice_x = file[f"{x_axis.lower()}"]
    user_choice_y = file[f"{y_axis.lower()}"]
    return user_choice_x, user_choice_y


x, y = get_data()

figure = px.scatter(x=x, y=y, labels={
    "x": f"{str(x_axis)}",
    "y": f"{str(y_axis)}"
})

st.plotly_chart(figure, kind="scatter")
