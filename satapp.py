import streamlit as st
import pandas as pd
import numpy as np

st.title('College Exam Results')

data = pd.read_csv("SAT.csv")
df_without_column = data.drop(columns=["DBN"])

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_without_column)

df = df_without_column.set_index('Number of Test Takers')

selected_columns = ['Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']

selected_data = df[selected_columns]

st.subheader('Barchart of Test Results per Tests Taken')
st.bar_chart(selected_data, use_container_width=True)

option = st.selectbox(
    'Which school would you like to see?',
     df_without_column['School Name'])

selected_school = df_without_column[df_without_column['School Name'] == option]

# Display bar chart
st.bar_chart(selected_school.set_index('School Name')[selected_columns])

