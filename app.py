import streamlit as st
import pandas as pd
import plotly.figure_factory as ff


st.title("Streamlit Basics practice")
test='hello there'
st.write('lets lerarn Streamlit')
st.write(test)
st.title("__Streamlit__ is cool", text_alignment='center')
st.write(':orange[your text here]')
st.header('This is a header')
st.subheader('This is a subheader')
st.markdown('This is a markdown')
st.caption('This is a caption')
st.markdown('This is a markdown ')
st.text('This is a text')
name=st.text_input('Enter your name')
st.write('Your name is:', name)
age=st.number_input('Enter your age', 0,10,5)
score=st.slider('Enter your score', 0,100,50)

from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.bar_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],
)

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(
    df,
    x="a",
    y=["b", "c"],
    color=["#FF0000", "#0000FF"],
)
