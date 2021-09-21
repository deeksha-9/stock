import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model


 start =  '2015-05-27'
 end = '2020-05-26'
st.title('Stock Pridiction App')

#@st.cache(allow_output_mutation=True)
user_input =  st.tet_input('Enter  Stock Ticker', 'AAPL')
df = data.DataReader(user_input, 'yahoo', start, end)

st.subheader('Data from 2015 - 2020')
st.write(df.describe())

st.subheadere('Closing Price vs Time chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA')
ma100 =  df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA')
ma100 =  df.Close.rolling(100).mean()
ma200 =  df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(ma100)
plt.plot(df.close)
st.pyplot(fig)


#plt.plot(day_new,sc.inverse_transform(df1[1159:]))
#plt.plot(day_pred,sc.inverse_transform(lst_output))
