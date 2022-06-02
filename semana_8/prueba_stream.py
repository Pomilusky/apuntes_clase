import streamlit as st
import pandas as pd

st.title('Titanic Dataset')  # titulo

st.header('Data from Titanic passengers') # cabecera de la tabla

df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
st.write(df)  # dataframe

st.header('Fare Cumulative')
fare=df['fare'].cumsum()
st.line_chart(fare)  # grafico de linea

st.write(sum(fare))