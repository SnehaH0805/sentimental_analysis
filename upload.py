import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title('CSV Uploader and Pie Chart Generator')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("DataFrame:")
    st.write(df)

    # Select column for pie chart
    column = st.selectbox("sentiment", df.columns)

    # Generate pie chart
    if st.button('Generate Pie Chart'):
        data = df['sentiment'].value_counts()

        fig, ax = plt.subplots()
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

        st.pyplot(fig)
