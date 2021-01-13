import news_config
import twitterbot
import google_nlp_config


# Get the headlines of the day
def get_headlines():
    news = news_config.NewsAPIConfiguration()
    return news.headlines_with_urls()


# Post to Twitter
def send_news_to_twitter():
    headlines_and_urls = get_headlines()

    # Pass the list of headlines to get the good news
    good_news = good_news_of_the_day(list(headlines_and_urls.keys()))

    tweet = good_news + "\n" + headlines_and_urls.get(good_news, "")
    twitterbot.post_tweet(tweet)


# Use the Google NLP API to fetch the good news of the day
def good_news_of_the_day(headlines):
    minimum_score = 0
    good_news = "Come back sometime later for a good news. So far it has all been sad news :( "

    for headline in headlines:
        headline_score = sentiment(headline)

        if headline_score > minimum_score:
            good_news = headline
            minimum_score = headline_score

    return good_news


# Analyze the sentiment of a headline
def sentiment(headline):
    sentiment_analyzer = google_nlp_config.SentimentAnalyzer()
    return sentiment_analyzer.sentiment_result(headline)


send_news_to_twitter()
