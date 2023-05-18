import streamlit as st
from files import functions as fn

todos = fn.list_r()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["Add"]
    todos.append(todo + "\n")
    fn.todos_w(todos)


st.title("My todo app")
st.write("<h4> \
         Check the box to <b>delete</b> the todo \
         </h4>",
         unsafe_allow_html=True)
st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="Add")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.todos_w(todos)
        del st.session_state[todo]
        st._rerun()
