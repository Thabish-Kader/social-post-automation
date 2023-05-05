import os
from github import Github
from dotenv import load_dotenv

load_dotenv()
acess_token = os.environ.get('ACESS_TOKEN')

g = Github(acess_token)
latest_repo = None
for repo in g.get_user().get_repos():
    if not latest_repo or repo.updated_at > latest_repo.updated_at:
        latest_repo = repo

if latest_repo:
    print("Latest repo:", latest_repo.name)
else:
    print("No repos found.")

