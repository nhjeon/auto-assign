import os
from typing import List

# Authentication is defined via github.Auth
from github import Auth
from github import Github

# using an access token
auth = Auth.Token(os.getenv('TOKEN'))

g = Github(auth=auth)
g = Github(base_url=f"{os.getenv('GITHUB_API_URL')}", auth=auth)

print(f"{os.getenv('GITHUB_REF')}")
#refs/pull/<pr_number>/merge


repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'), lazy=True)

print(os.getenv('REVIEWERS'))

pulls = repo.get_pulls(state='open')
for pr in pulls:
    print(pr.assignees)
    pr.add_to_assignees(pr.user.name)
    print(pr)
    print(pr.assignees)
    print(pr.assignees)
    pr.add_to_assignees(pr.user.login)
    print(pr)
    print(pr.assignees)

def assign_reviewer(branch: str, reviewer: List[str], github: Github):
    pass

def assign_reviewee(branch: str, reviewer: List[str], github: Github):
    pass