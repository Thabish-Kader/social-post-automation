import os
from github import Github
from dotenv import load_dotenv
from linkedin_api import Linkedin
import tweepy

load_dotenv()
acess_token = os.environ.get('ACESS_TOKEN')
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_KEY_SECRET')
twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

#  ----- Github ------ 
g = Github(acess_token)
latest_repo = None
# Loop over repos and find the latest repo
for repo in g.get_user().get_repos():
    if not latest_repo or repo.updated_at > latest_repo.updated_at:
        latest_repo = repo
contents = latest_repo.get_contents("readme.md")
readme_content = contents.decoded_content.decode("utf-8")


# ----- Twitter ------
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    twitter_access_token, twitter_access_token_secret
)
api = tweepy.API(auth)
print(api.get_friends())
# api.update_status("Hello world")
# if latest_repo :
#     print("Do you want to post the latest repo on Twitter ?")
#     answer = input("Y/N : ")
#     if answer.lower() == "y" :
#         try :
#             tweet_text=f"Check out my latest GitHub repository: {latest_repo.repo_name} - {latest_repo.repo_description} {latest_repo.repo_url}"
#             api.update_status(tweet_text)
#             print("Posted on Twitter!")
#         except PermissionError:
#             print("Unable to post on Twitter")
#     else:
#         print("Not sharing to Twitter")
# else:
#     print("No repo found")


