import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob


def show():
    # Set up the Streamlit app
    st.title('Sentiment Analysis with Emojis')
    st.write('Enter text to analyze its sentiment.')

    user_input = st.text_area("Enter your text here:")

    if user_input:
        # Perform sentiment analysis
        def analyze_sentiments(text):
            blob = TextBlob(text)
            return blob.sentiment.polarity

        polarity = analyze_sentiments(user_input)

        # Classify sentiments as very positive, positive, neutral, negative, or very negative
        def classify_sentiments(polarities):
            if polarities > 0.5:
                return 'Very Positive 😍'
            elif polarities > 0:
                return 'Positive 🙂'
            elif polarities == 0:
                return 'Neutral 😐'
            elif polarities > -0.5:
                return 'Negative 🙁'
            else:
                return 'Very Negative 😠'

        sentiment_classs = classify_sentiments(polarity)

        # Display the results
        st.write(f"Sentiment Score: {polarity:.2f}")
        st.write(f"Sentiment Class: {sentiment_classs}")

        # Plotting the pie chart with emojis
        fig, ax = plt.subplots()
        ax.pie([1], labels=[sentiment_classs], autopct='%1.1f%%', startangle=90, colors=['#ff9999'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart
        st.pyplot(fig)
    else:
        st.error("Please enter some text to analyze.")