import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Best Todo App This World's Ever Seen")
st.subheader("Alright")
st.write("This app is to make you feel unproductive.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="1", label_visibility='hidden',
              placeholder="Add a task here..",
              on_change=add_todo, key='new_todo')
