import os
from newsapi import NewsApiClient


class NewsAPIConfiguration:
    def __init__(self):
        self.__news_api_key = os.environ["NEWS_API_KEY"]
        self.__news = NewsApiClient(self.__news_api_key)

    def get_api(self):
        return NewsApiClient(api_key=self.__news_api_key)

    def headlines_with_urls(self):
        headline_urls = {}
        headlines = self.__news.get_top_headlines()

        for article in headlines['articles']:
            headline_urls[article['title']] = article['url']

        return headline_urls
