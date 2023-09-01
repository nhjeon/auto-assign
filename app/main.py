import os
from typing import List

# Authentication is defined via github.Auth
from github import Auth
from github import Github

# using an access token
auth = Auth.Token(os.getenv('TOKEN'))

g = Github(auth=auth)
g = Github(base_url=f"{os.getenv('GITHUB_API_URL')}", auth=auth)

# Then play with your Github objects:

print(f"{os.getenv('GITHUB_REPOSITORY')}")
print(f"{os.getenv('GITHUB_BASE_REF')}")
print(f"{os.getenv('GITHUB_REF')}")
print(f"{os.getenv('TOKEN')}")


repo = g.get_repo("nhjeon/auto_assign_test", lazy=True)

pulls = repo.get_pulls(state='open')
for pr in pulls:
    print(pr.number)



def assign_reviewer(branch: str, reviewer: List[str], github: Github):
    pass

def assign_reviewee(branch: str, reviewer: List[str], github: Github):
    pass