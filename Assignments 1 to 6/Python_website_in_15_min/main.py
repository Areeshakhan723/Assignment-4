import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.set_page_config(page_title="Data dashboard", page_icon="📊", layout="centered")

st.title("Simple Data dashboard")

uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select a value", unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader("Data plot")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file uploader...")