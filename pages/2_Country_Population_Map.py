import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('world_population.csv')

df['Country Code'] = df['CCA3']

year = st.sidebar.selectbox('Select Year', ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population'])

fig = px.choropleth(
    df,
    locations='Country Code',
    color=year,
    hover_name='Country',
    hover_data=[year, 'Capital'],
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f'World Population in {year.split()[0]}',
)

st.plotly_chart(fig)