import os
from typing import List

# Authentication is defined via github.Auth
from github import Auth
from github import Github

# using an access token
auth = Auth.Token("access_token")

g = Github(auth=auth)
g = Github(base_url=f"{os.getenv('GITHUB_API_URL')}/api/v3", auth=auth)

# Then play with your Github objects:

print(f"{os.getenv('GITHUB_PATH')}")
print(f"{os.getenv('GITHUB_REPOSITORY')}")
print(f"{os.getenv('GITHUB_BASE_REF')}")
print(f"{os.getenv('GITHUB_REF')}")

repo = g.get_repo("nhjeon/auto_assign_test")


def assign_reviewer(branch: str, reviewer: List[str], github: Github):
    pass

def assign_reviewee(branch: str, reviewer: List[str], github: Github):
    pass