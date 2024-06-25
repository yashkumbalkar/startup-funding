import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('i am learning streamlit')
st.subheader('and i am loving it')

st.write('This is normal text')

st.markdown('''
### My favourite movies
- Race
- Hamshakals
- Housefull
''')

st.code('''
def foo(i):
    return i**2

foo(2)
''')

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame(
    {
        'name': ['nitish', 'ankit', 'anup'],
        'marks': [50, 60, 70],
        'package': [10, 12, 14]
    }
)

st.dataframe(df)

st.metric('Revenue', 'Rs. 3L', '+3%')

st.json({
    'name': ['nitish', 'ankit', 'anup'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.image('b1.jpg')

st.video('song.mp4')

st.sidebar.title('Sidebar')

col1, col2 = st.columns(2)

with col1:
    st.image('b2.jpg')

with col2:
    st.image('b3.jpg')

st.error('Login failed')
st.success('Login success')
st.info('Normal message')
st.warning('Warning')

'''
bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.2)
    bar.progress(i)

'''

email = st.text_input('Enter Email')
number = st.number_input('Enter Age')
date = st.date_input('Enter date')

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select Gender',['male','female'])

btn = st.button('Login')

if btn:
    if email == 'yash@gmail.com' and password == '123':
        st.success('Login Successful')
    else:
        st.error('Incorrect email or password')

file = st.file_uploader('upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())

