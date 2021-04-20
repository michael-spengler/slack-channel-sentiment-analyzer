# Reference: https://www.codeproject.com/Articles/5269445/Using-Pre-trained-VADER-Models-for-NLTK-Sentiment

import nltk

nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(statement):
  scores = analyzer.polarity_scores(statement)

  # The compound value reflects the overall sentiment
  # ranging from -1 being very negative and +1 being very positive.
  print(statement, scores)
  return scores['compound']