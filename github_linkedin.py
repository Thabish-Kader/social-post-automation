#!/usr/bin/python3

import os
from github import Github
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get('GITHUB_PASSWORD')

# using username and password
g = Github("Thabish-Kader", password)

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     repo.edit(has_wiki=False)