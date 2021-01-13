import tweepy
import os


class TwitterConfiguration:

    def __init__(self):
        # Initialize the API Secret
        self.__consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
        self.__consumer_secret = os.environ["TWITTER_CONSUMER_KEY_SECRET"]
        self.__access_token = os.environ["TWITTER_APP_ACCESS_TOKEN"]
        self.__access_token_secret = os.environ["TWITTER_APP_ACCESS_TOKEN_SECRET"]

    def handle_auth(self):
        return tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)

    def access_token(self, auth):
        auth.set_access_token(self.__access_token, self.__access_token_secret)
