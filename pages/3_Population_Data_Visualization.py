import streamlit as st
import pandas as pd

data = pd.read_csv('world_population.csv')

countries = data['Country'].unique()

st.title('Country Population Data')

selected_country = st.selectbox('Select a country:', countries)

country_data = data[data['Country'] == selected_country]

st.subheader(f'Population Data for {selected_country}')

st.line_chart(country_data[['2022 Population', '2020 Population', '2015 Population', 
                            '2010 Population', '2000 Population', '1990 Population', 
                            '1980 Population', '1970 Population']].T)

st.subheader('Additional Information')
st.write(country_data)