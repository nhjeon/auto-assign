import os
from typing import List

# Authentication is defined via github.Auth
from github import Auth
from github import Github

# using an access token
auth = Auth.Token("access_token")

g = Github(auth=auth)
g = Github(base_url="https://github.com/api/v3", auth=auth)

# Then play with your Github objects:

print(f"asdf{os.getenv('TOKEN')}asdf")
print(f"asdf{os.getenv('GITHUB_REPOSITORY')}asdf")
print(f"asdf{os.getenv('GITHUB_BASE_REF')}asdf")
print(f"asdf{os.getenv('GITHUB_API_URL')}asdf")

def assign_reviewer(branch: str, reviewer: List[str], github: Github):
    pass

def assign_reviewee(branch: str, reviewer: List[str], github: Github):
    pass