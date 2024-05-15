import streamlit as st
import time
import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('world_population.csv')

# Set page configuration
st.set_page_config(page_title="Global Population Plot", page_icon="📊")

# Set up the main title and sidebar
st.markdown("# Global Population Plot")
st.sidebar.header("Global Population Plot")
st.write(
    """This demo illustrates an animated plot with Streamlit. We're generating a random walk for 
    global population data over time. Enjoy!"""
)

# Initialize the progress bar, status text, and chart
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.empty()

# Define population columns and years
population_columns = ['1970 Population', '1980 Population', '1990 Population', '2000 Population',
                      '2010 Population', '2015 Population', '2020 Population', '2022 Population']

years = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]

# Iterate over the years to create the animated plot
for i, year in enumerate(years):
    chart_data = pd.DataFrame({
        "Year": years[:i + 1],
        "Global Population": [df[col].sum() for col in population_columns[:i + 1]]
    })

    # Update status
    status_text.text(f"Year: {year}")

    # Update chart
    chart.line_chart(chart_data, x="Year", y="Global Population")

    # Update progress bar
    progress_bar.progress(int((i + 1) / len(years) * 100))

    # Pause for a short time to create animation effect
    time.sleep(0.5)

# Clear the progress bar
progress_bar.empty()

# Add a re-run button
st.button("Re-run")
