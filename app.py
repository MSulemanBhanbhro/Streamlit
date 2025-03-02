import streamlit as st 
import pandas as pd
import numpy as np



st.title("Mera Pahela Streamlit")
st.write("Asalam o alaikum ye mea pahela web app hai")
st.header("ye header he")
st.subheader("ye sub header he")
st.text("ye aik simple text he")

name = st.text_input("Apna Nam Likhen")
age = st.number_input("Apni Umar Likhen", min_value=1, max_value=100)
agree = st.checkbox("Main Agree Krta hun")
gender = st.radio("Apna Gender Select kren", ["Male","Female"])

if st.button("Submit"):
    st.success(f"Shukria {name} , aap {age} sall k hen")

if st.button("Click me"):
    st.write("Aap ne button click kia")

st.image("logo.png", caption="Ye aik logo image", use_column_width = True)

chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=["A","B","C","D"]
)
st.line_chart(chart_data)

st.sidebar.title("Mera Side Bar")
st.sidebar.button("Click Me !")

menu = st.sidebar.selectbox("Choose page", ["Home","About","Contact"])
if menu == "Home":
    st.write("Welcome to home page")
elif menu == "About":
    st.write("Welcome to About Page")
elif menu == "Contact":
    st.write("Welcome to Contact Page")
