# Sentiment Analysis Tool

Welcome to the Sentiment Analysis Tool! This tool allows you to analyze the sentiment of a given text using a simple web interface built with Streamlit.

## Features

- Analyze the sentiment of any given text.
- Displays polarity and subjectivity scores.
- Qualitative sentiment results: Positive, Negative, or Neutral.
- Easy-to-use web interface.
To get started with the Sentiment Analysis Tool, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone (https://github.com/SnehaH0805/sentimental_analysis.git)
   cd sentiment_nalysis

2. **Create and activate a virtual environment (optional but recommended)**:
   python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **pip install -r requirements.txt**
   pip install -r requirements.txt

   
   **To run the Sentiment Analysis Tool locally, use the following command:**

   streamlit run demo.py

This will start a local Streamlit server, and you can access the tool in your web browser at http://localhost:8501.

--------------------------------------------------------------------------------------------------------------------------------------------

**First screen of web app Home Page**

default page is home page as shown below:
![image](https://github.com/SnehaH0805/sentimental_analysis/assets/172985386/2e93513f-629d-421c-8f07-684768636229)

**2nd screen sentimental analysis with emoji**

In navigation panel select sentimental analysis with emoji .
The Sentiment Analysis Tool allows you to analyze the sentiment of individual reviews or text inputs effortlessly. Using the power of natural language processing (NLP), this tool evaluates the sentiment behind a piece of text and provides a comprehensive sentiment analysis. Here’s how it works:

How It Works
Input Text: Enter the text you want to analyze in the provided text area.
Analyze Sentiment: Click the "Enter" button to process the text.

Sentiment Results:
Polarity: A value between -1 and 1, indicating how negative or positive the text is. A negative score indicates negative sentiment, a positive score indicates positive sentiment, and a score around zero indicates neutral sentiment.

Subjectivity: A value between 0 and 1 that tells how subjective or objective the text is. A score closer to 1 indicates a subjective statement (opinion), while a score closer to 0 indicates an objective statement (fact).

![image](https://github.com/SnehaH0805/sentimental_analysis/assets/172985386/b7a96ffa-39f4-4f1b-909c-853976126399)

**3rd screen Upload CSV and Generate Sentiment Analysis Chart**
In neveigation panel select Upload CSV and Generate Sentiment Analysis Chart:

Upload CSV and Generate Sentiment Analysis Chart
The Sentiment Analysis Tool allows you to analyze the sentiment of multiple text entries by uploading a CSV file and generating visual sentiment analysis charts. This feature helps you gain insights into the overall sentiment trends in your data, making it easier to visualize and understand the results.

How It Works
Upload CSV File: Upload a CSV file containing the text data you want to analyze. The CSV file should have a column with the text entries you wish to analyze.

Select Column: Choose the column from the uploaded CSV that contains the text data.  (Example file:[amazon_review.csv](https://github.com/user-attachments/files/15936244/amazon_review.csv)
  )

Analyze Sentiment: Click the "Analyze" button to process all the text entries in the selected column.

View Results: The tool generates sentiment analysis charts that visualize the distribution of polarity (positive, negative, neutral) and subjectivity (subjective, objective) scores.

![screencapture-localhost-8501-2024-06-22-15_46_25](https://github.com/SnehaH0805/sentimental_analysis/assets/172985386/4de559a2-ab1f-4fe4-9944-4eda5afd02b8)

Visual Insights: Provides visual representations of sentiment analysis results, making it easier to understand and communicate findings.

Trend Analysis: Helps identify sentiment trends over time or across different categories.

Batch Processing: Efficiently analyze and visualize the sentiment of large datasets.

This feature is ideal for businesses and researchers who need to process and visualize the sentiment of large volumes of text data, making it easier to derive actionable insights.
