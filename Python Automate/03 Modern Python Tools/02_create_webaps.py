import streamlit as st 
import pandas
#run with: streamlit run '.\03 Modern Python Tools\02_create_webaps.

data = {
    'Series_1':[1, 2, 3, 4, 5, 7],
    'Series_2':[10, 30, 40, 100, 250, 280]
}
df = pandas.DataFrame(data)

st.title('Our first streamlit app')
st.subheader('Introducing Streamlit in automate everything with Python')
st.write('''This is our first Web App
         Enjoy it''')
st.write(df)
st.line_chart(df)

myslider = st.slider('Celcius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)