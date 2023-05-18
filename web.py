import streamlit as st
from files import functions as fn

todos = fn.list_r()


def add_todo():
    todo = st.session_state["Add"]
    todos.append(todo + "\n")
    fn.todos_w(todos)


st.title("My todo app")
st.subheader("Check the box to delete the todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.todos_w(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="Add")
