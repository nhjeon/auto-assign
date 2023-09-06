import os


class GithubEnv:

    def __repr__(self):
        return f'GithubEnv(repository="{self.repository}", pr_number="{self.pr_number}")'

    @staticmethod
    def _parse_pr_number(github_ref: str):
        split_github_ref = github_ref.split('/')

        if len(split_github_ref) != 4:
            raise ValueError(f'invalid literal for _parse_pr_number(): "{github_ref}"')

        if not split_github_ref[2].isdigit():
            raise ValueError(f'invalid literal for split_github_ref[2]: "{split_github_ref[2]}"')

        return int(split_github_ref[2])

    def __init__(self):
        self.token = os.getenv('TOKEN')

        self.repository = os.getenv('GITHUB_REPOSITORY')

        self.pr_number = self._parse_pr_number(
            os.getenv('GITHUB_REF')
        )

        if not self.token:
            raise ValueError('github token is None')

        if not self.pr_number:
            raise ValueError('github pr_number is None')


class AppEnv:

    def __repr__(self):
        return f'AppEnv(reviewers={self.reviewers})'

    def __init__(self):
        self.reviewers = [i.replace(' ', '') for i in os.getenv('REVIEWERS', "nhjeon, tndyd5390").split(',')]
