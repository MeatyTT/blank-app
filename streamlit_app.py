import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# @st.cache_resource
# def create_list():
#     l = [1, 2, 3]
#     return l

# l = create_list()
# first_list_value = l[0]
# l[0] = first_list_value + 1

# st.write("l[0] is:", l[0])
df = pd.DataFrame({
    'first-column':[1,2,3,4],
    'second-column':[10,20,30,40]
})
# st.write("Hello World")
df

st.write("Bang test")
st.table(pd.DataFrame({
    'first-column':[1,2,3,4],
    'second-column':[10,20,30,40]
}))
x = st.slider('x',max_value=100)  # 👈 this is a widget
st.write(x, 'squared is', x ** 2)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.write("Your name is",st.session_state.name)
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
# df['first column']
option = st.selectbox(
    'Which number do you like best?',
     [1,2]
)
if option ==1:
    x = df['first column']
else:
    x = df['second column']
'You selected: ', x
