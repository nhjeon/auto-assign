from github import Auth, GithubException
from github import Github

from env import GithubEnv, AppEnv

github_env = GithubEnv()
app_env = AppEnv()

print(github_env)
print(app_env)

github = Github(auth=Auth.Token(github_env.token))
repo = github.get_repo(github_env.repository, lazy=True)
pr = repo.get_pull(number=github_env.pr_number)

pr.add_to_assignees(pr.user)
print(f"assignee: {pr.assignees}")

for i in app_env.reviewers:
    try:
        pr.create_review_request([i])
    except GithubException as e:
        print(f"{e.data['message']}: {i}")
print(f"reviewers: {pr.requested_reviewers}")
