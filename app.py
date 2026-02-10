import streamlit as st
import pickle

with open("stock_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Stock Prediction")

st.title("Stock Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    open_price = st.number_input("Open Price", value=1500.0, step=1.0)
    high_price = st.number_input("High Price", value=1520.0, step=1.0)
    low_price = st.number_input("Low Price", value=1490.0, step=1.0)
    close_price = st.number_input("Close Price", value=1510.0, step=1.0)

with col2:
    volume = st.number_input("Volume Traded", value=1000000.0, step=10000.0)
    market_cap = st.number_input("Market Cap", value=800000000000.0, step=1000000000.0)
    pe_ratio = st.number_input("PE Ratio", value=25.0, step=0.1)
    dividend_yield = st.number_input("Dividend Yield", value=1.5, step=0.1)

with col3:
    eps = st.number_input("EPS", value=50.0, step=0.1)
    week52_high = st.number_input("52 Week High", value=1600.0, step=1.0)
    week52_low = st.number_input("52 Week Low", value=1200.0, step=1.0)


input_data = [[
    open_price, 
    high_price,
    low_price,
    close_price,
    volume,
    market_cap,
    pe_ratio,
    dividend_yield,
    eps,
    week52_high,
    week52_low
]]

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Next Close Price: {prediction:.3f}")
