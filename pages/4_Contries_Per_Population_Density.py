import streamlit as st
import pandas as pd

df = pd.read_csv("world_population.csv")

top_five_density = df.nlargest(5, 'Density (per km²)')
st.subheader("Population Density of Top 5 Countries")
st.bar_chart(top_five_density[['Country', 'Density (per km²)']].set_index('Country'))