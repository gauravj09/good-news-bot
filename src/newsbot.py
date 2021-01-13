import news_config
import twitterbot
import google_nlp_config


# Get the headlines of the day
def get_headlines():
    news = news_config.NewsAPIConfiguration()
    return news.news_headlines()


# Post to Twitter
def send_news_to_twitter():
    headlines = get_headlines()

    good_news = good_news_of_the_day(headlines)
    twitterbot.post_tweet(good_news)


# Use the Google NLP API to fetch the good news of the day
def good_news_of_the_day(headlines):
    minimum_score = 0
    good_news = "Come back sometime later for a good news. So far it has all been sad news :( "

    for headline in headlines:
        headline_analysis = sentiment(headline)

        if headline_analysis > minimum_score:
            good_news = headline
            minimum_score = headline_analysis

    return good_news


# Analyze the sentiment of a headline
def sentiment(headline):
    analyzer = google_nlp_config.SentimentAnalyzer()
    return analyzer.sentiment_result(headline)


send_news_to_twitter()
