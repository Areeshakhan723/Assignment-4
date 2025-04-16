import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]
        return name , capital, population, area, currency, region
    else:
        None


def main():
    st.set_page_config(page_title="Country Information Card", page_icon="🌍")

    st.title("Country Information Card 🌍")   

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.subheader(f"Country Information")
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area} square kilometers")
            st.write(f"Currency: {', '.join(currency.keys())}")
            st.write(f"Region: {region}")          
        else:
            st.error("Country not found. Please try again.")     


if __name__ == "__main__":
    main()            