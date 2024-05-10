import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center;'>IMDB Movie Data</h1>", unsafe_allow_html=True)

df = pd.read_csv("imdb_movie_data.csv") #path folder of the data file
result = st.data_editor(df, num_rows='dynamic')

edited_df = pd.DataFrame(result)
chartdata = edited_df[['movie', 'imdb_rating', 'vote']]
top_5_imdb_rating = chartdata.nlargest(5, 'imdb_rating')
st.write("Top 5 movies by IMDb rating:")
st.bar_chart(top_5_imdb_rating.set_index('movie')['imdb_rating'])
chart_data = edited_df[["vote", 'year']]
st.line_chart(chart_data.set_index('year')['vote'])
