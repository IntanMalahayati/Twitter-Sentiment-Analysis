# Twitter-Sentiment-Analysis

This project focuses on performing sentiment analysis on Twitter data using Python. The goal is to analyze the sentiment (positive or negative) of tweets based on a lexicon.

## Project Overview

- Data Source: Twitter data, scraped using the `Twint` library.
- Keywords: Data scraped from Twitter using different keywords for sentiment analysis.
- Language: Python
- Approach: Preprocessing of text data followed by sentiment analysis using a lexicon-based approach.

## Workflow

### Data Scraping:

Used the `Twint` library to scrape Twitter data without needing Twitter's API.
Data is filtered based on specific keywords to capture relevant tweets for analysis.

### Data Preprocessing:

Cleaned and preprocessed the text data by removing unnecessary characters, stopwords, and performing tokenization.
Ensured the text was ready for analysis by normalizing and standardizing the format.

### Sentiment Analysis:

Used a lexicon-based approach to classify the sentiment of each tweet.
The analysis was based on predefined positive and negative lexicons to determine the overall sentiment polarity.

## Installation

To run this project, we need to install the following dependencies:

#### `Twint` Installation

```bash
pip3 install twint
```

#### Other Dependencies

Install the additional libraries used in this project:

```bash
pip install nltk
```

## Technologies Used

- Python
- `Twint` (for data scraping)
- NLTK (for text preprocessing)
- Lexicon-based sentiment analysis

## Results

The project provides insights into how people express sentiments on Twitter related to the selected keywords, categorized into positive and negative sentiments.
