import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a data visualization above.")

st.markdown(
    """
    Come one and Come all, to the greatest website in all the land. Here we will show you all the global population
    you could ever dream of
"""
)
st.image(image="world.jpg")
st.write("We beat Covid-19 but can we beat Goku")
st.audio("Ultra Instinct.mp3", loop=True, autoplay=True)