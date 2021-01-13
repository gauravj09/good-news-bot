import os
from newsapi import NewsApiClient


class NewsAPIConfiguration:
    def __init__(self):
        self.__news_api_key = os.environ["NEWS_API_KEY"]
        self.__news = NewsApiClient(self.__news_api_key)

    def get_api(self):
        return NewsApiClient(api_key=self.__news_api_key)

    def news_headlines(self):
        list_of_headlines = []
        headlines = self.__news.get_top_headlines()

        for article in headlines['articles']:
            list_of_headlines.append(article['title'])

        return list_of_headlines
