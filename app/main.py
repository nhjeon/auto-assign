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

print()


reviewers = [i.replace(' ', '') for i in  os.getenv('REVIEWERS').split(',')]

pulls = repo.get_pulls(state='open')
for pr in pulls:
    print(pr.id)
    print(pr.add_to_assignees(pr.user.login))
    print(pr.assignees)
    print(pr.create_review_request(reviewers))
    print(pr.requested_reviewers)


def assign_reviewer(branch: str, reviewer: List[str], github: Github):
    pass

def assign_reviewee(branch: str, reviewer: List[str], github: Github):
    pass