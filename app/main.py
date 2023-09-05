from typing import List

from github import Auth, GithubException, PullRequest, NamedUser
from github import Github

from env import GithubEnv, AppEnv


def get_pr(token: str, repository: str, pr_number: int):
    github = Github(auth=Auth.Token(token))
    repo = github.get_repo(repository, lazy=True)
    return repo.get_pull(number=pr_number)


def add_to_assignee(_pr: PullRequest, named_user: NamedUser):
    _pr.add_to_assignees(named_user)
    print(f"assignee: {_pr.assignees}")


def add_to_reviewers(_pr: PullRequest, reviewer_list: List[str]):
    for i in reviewer_list:
        try:
            _pr.create_review_request([i])
        except GithubException as e:
            print(f"{e.data['message']}: {i}")
    print(f"reviewers: {_pr.requested_reviewers}")


def add_task_description(_pr: PullRequest):
    issue_comment = list(
        filter(
            lambda x: not x.startswith("- Merge pull request"),
            map(
                lambda x: f"- {x.commit.message}",
                _pr.get_commits()
            )
        )
    )
    issue_comment.insert(0, "작업 내역")
    _pr.create_issue_comment("\n".join(issue_comment))


if __name__ == "__main__":
    github_env = GithubEnv()
    app_env = AppEnv()

    print(github_env)
    print(app_env)

    pr = get_pr(github_env.token, github_env.repository, github_env.pr_number)
    add_to_assignee(pr, pr.user)
    add_to_reviewers(pr, app_env.reviewers)
    add_task_description(pr)
