from typing import List

from github import Github, Auth, NamedUser, GithubException


class GithubPullRequest:

    def __init__(self, token: str, repository_name: str, pr_number: int):
        github = Github(auth=Auth.Token(token))
        repository = github.get_repo(repository_name, lazy=True)
        self.pull_request = repository.get_pull(number=pr_number)

    @property
    def user(self):
        return self.pull_request.user

    def add_assignee(self, named_user: NamedUser):
        self.pull_request.add_to_assignees(named_user)
        print(f"assignee: {self.pull_request.assignees}")

    def add_reviewers(self, reviewer_list: List[str]):
        for i in reviewer_list:
            try:
                self.pull_request.create_review_request([i])
            except GithubException as e:
                print(f"{e.data['message']}: {i}")
        print(f"reviewers: {self.pull_request.requested_reviewers}")

    def add_task_description(self):
        issue_comment = list(
            filter(
                lambda x: not x.startswith("- Merge pull request"),
                map(
                    lambda x: f"- {x.commit.message}",
                    self.pull_request.get_commits()
                )
            )
        )
        issue_comment.insert(0, "작업 내역")
        self.pull_request.create_issue_comment("\n".join(issue_comment))
