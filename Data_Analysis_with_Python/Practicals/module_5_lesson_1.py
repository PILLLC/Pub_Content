from textblob import TextBlob

# Sample text for demonstration
text = "TextBlob is a simple and easy-to-use library for text processing tasks. I love using it!"

# Tokenization
blob = TextBlob(text)
tokens = blob.words

print("Tokens:")
print(tokens)

# Sentiment Analysis
sentiment = blob.sentiment
polarity = sentiment.polarity
subjectivity = sentiment.subjectivity

print("\nSentiment Analysis:")
print("Polarity:", polarity)
print("Subjectivity:", subjectivity)