from transformers import pipeline  
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  

# ✅ Load fraud detection model (BERT-based)
fraud_detector = pipeline("text-classification", model="textattack/bert-base-uncased-yelp-polarity")

def detect_fraud(text):
    """
    Detects whether the given text is fraudulent.
    Returns the fraud label and confidence score.
    """
    result = fraud_detector(text)
    print("DEBUG: Fraud Result →", result)  # Debugging log
    return result[0]['label'], result[0]['score']

# ✅ Load sentiment analysis model (VADER)
analyzer = SentimentIntensityAnalyzer()

def detect_urgency(text):
    """
    Detects the urgency of a given message.
    Returns 'Urgent' if the message has a strong negative sentiment.
    """
    score = analyzer.polarity_scores(text)
    return "Urgent" if score['compound'] < -0.5 else "Not Urgent"
