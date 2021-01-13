import tweepy
from twitter_config import TwitterConfiguration


# Verify the credentials using the Twitter Configuration class
def configure():
    auth = TwitterConfiguration().handle_auth()
    TwitterConfiguration().access_token(auth)
    return tweepy.API(auth)


# Read the posts on home timeline
def home_timeline_tweets():
    api = configure()

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


# Post tweets to the configured twitter handle
def post_tweet(text):
    api = configure()
    api.update_status(text)
