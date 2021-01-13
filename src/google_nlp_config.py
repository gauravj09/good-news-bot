# Imports the Google Cloud client library
from google.cloud import language_v1


def analyze_text(text):
    return language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)


class SentimentAnalyzer:
    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def sentiment_analysis(self, text):
        document = analyze_text(text)
        return self.client.analyze_sentiment(request={'document': document}).document_sentiment

    def sentiment_result(self, text):
        print("Text: {}".format(analyze_text(text)))
        print("Sentiment: {}, {}".format(self.sentiment_analysis(text).score, self.sentiment_analysis(text).magnitude))
        return self.sentiment_analysis(text).score


