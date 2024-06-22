import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Sentiment Analysis with Emojis", "Upload CSV and Generate Pie Chart"])

    if page == "Home":
        home()
    elif page == "Upload CSV and Generate Pie Chart":
        upload_and_pie_chart()
    elif page == "Sentiment Analysis with Emojis":
        textanalysis()


def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")


def upload_and_pie_chart():
    st.title('CSV Uploader and Pie Chart Generator')
    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Select column
        column = st.selectbox("Select the column for sentiment analysis", df.columns)

        if st.button("Analyze Sentiment"):
            # Perform sentiment analysis
            def analyze_sentiment(text):
                blob = TextBlob(text)
                return blob.sentiment.polarity

            df['Sentiment'] = df[column].astype(str).apply(analyze_sentiment)

            # Classify sentiments as positive, neutral, or negative
            def classify_sentiment(polarity):
                if polarity > 0:
                    return 'Positive'
                elif polarity < 0:
                    return 'Negative'
                else:
                    return 'Neutral'

            df['Sentiment_Class'] = df['Sentiment'].apply(classify_sentiment)

            # Count the occurrences of each sentiment class
            sentiment_counts = df['Sentiment_Class'].value_counts()

            # Plotting the pie chart
            fig, ax = plt.subplots()
            ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Display the pie chart
            st.pyplot(fig)

            # Display bar chart for sentiment scores
            st.bar_chart(df['Sentiment_Class'].value_counts())

            # Show DataFrame with sentiment analysis
            st.write(df)


def textanalysis():
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


if __name__ == "__main__":
    main()
