import os
from github import Github
from dotenv import load_dotenv
from linkedin_api import Linkedin


load_dotenv()
acess_token = os.environ.get('ACESS_TOKEN')
linkedin_email = os.environ.get('LINKEDIN_EMAIL')
linkedin_password = os.environ.get('LINKEDIN_PASSWORD')

#  ----- Github ------ 
g = Github(acess_token)
latest_repo = None
# Loop over repos and find the latest repo
for repo in g.get_user().get_repos():
    if not latest_repo or repo.updated_at > latest_repo.updated_at:
        latest_repo = repo
content = latest_repo.get_contents("readme.md")

print(content)
# ----- LinkedIn ------
# linkedin_api = Linkedin(linkedin_email, linkedin_password)

