import streamlit as st 
import pandas as pandas
import pickle

date = st.date_input("Enter date")
ticker = st.number_input("Enter number")

if ticker < 0:
    st.error("pred")
else:
    st.success("pred")
input = [date,ticker]
with open("stock_model.pkl","rb") as f:
    model = pickle.load(f)
pred =  model.predict(input)
