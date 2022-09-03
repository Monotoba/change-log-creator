from datetime import datetime

from git import Repo


def create_change_log_from_repo(repo: str = None, max_count=50):

    if repo is not None:
        raise ValueError('A repository must be supplied!')

    local_repo = Repo(repo)

    commits = local_repo.iter_commits('master', max_count=max_count)

    now = datetime.now()
    output = f"# CHANGE LOG\n\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}\n\n"
    for commit in commits:
        output += f"```\n Date: {commit.authored_datetime}\n" \
                  f" Change: {commit.message}\n" \
                  f" Author: {commit.committer.name} <{commit.committer.email}>\n" \
                  f" Date Offset: {commit.author_tz_offset}\n" \
                  "```\n\n"

    return output




if __name__ == '__main__':
    repo = '~/projects/python-3/change-log-creator'
    text = create_change_log_from_repo()

    with open('CHANGELOG.md', 'w') as fho:
        fho.write(text)
