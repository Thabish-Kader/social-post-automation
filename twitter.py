import os
from github import Github
from dotenv import load_dotenv
from linkedin_api import Linkedin
import tweepy
import requests

load_dotenv()
acess_token = os.environ.get('ACESS_TOKEN')
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
twitter_bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=twitter_access_token, access_token_secret=twitter_access_token_secret
)
response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)

