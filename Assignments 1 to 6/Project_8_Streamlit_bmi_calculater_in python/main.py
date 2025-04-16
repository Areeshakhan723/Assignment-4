import streamlit as st  
import pandas as pd

st.set_page_config(page_title="BMI Calculator", page_icon=":weight_lifter:", layout="centered")
st.title("🧮 BMI Calculator")

height = st.slider("Enter your height (in cm)", 100, 250, 170)
weight = st.slider("Enter your weight (in kg)", 30, 200, 70)

# BMI calculation
bmi = weight / ((height / 100) ** 2)

st.subheader(f"Your BMI is: {bmi:.2f}")

st.write("### 🧾BMI Categories ###")
st.write("- Underweight: BMI less then 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")
