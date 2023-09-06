from env import GithubEnv, AppEnv
from github_pull_request import GithubPullRequest

if __name__ == "__main__":
    github_env = GithubEnv()
    app_env = AppEnv()

    print(github_env)
    print(app_env)

    pr = GithubPullRequest(
        token=github_env.token,
        repository_name=github_env.repository,
        pr_number=github_env.pr_number
    )

    pr.add_assignee(pr.user)
    pr.add_reviewers(app_env.reviewers)
    pr.add_task_description()
