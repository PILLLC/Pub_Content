
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('movie_reviews')

# Sentiment Analysis
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Text Classification
# Prepare training data
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
# Shuffle the documents
import random
random.shuffle(documents)

# Define features extractor
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# Train Naive Bayes classifier
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate classifier accuracy
print("Classifier Accuracy:", accuracy(classifier, test_set))

# Test sentiment analysis
text = "I love this movie. It's fantastic!"
print("Sentiment Analysis Result:", analyze_sentiment(text))

# Test text classification
text = "This movie is a masterpiece."
features = document_features(word_tokenize(text))
print("Text Classification Result:", classifier.classify(features))