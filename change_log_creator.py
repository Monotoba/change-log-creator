from git import Repo


def create_change_log_from_repo(repo: str = None, max_count=50):

    if repo is not None:
        raise ValueError('A repository must be supplied!')

    local_repo = Repo(repo)

    commits = local_repo.iter_commits('master', max_count=max_count)

    output = ''
    for commit in commits:
        output += f"```\nDate: {commit.authored_datetime}\n" \
                  f"Change: {commit.message}\n" \
                  f"Author: {commit.author} Date Offset: {commit.author_tz_offset}\n```\n\n"

    print(output)

if __name__ == '__main__':
    repor = '~/projects/python-3/change-log-creator'
    create_change_log_from_repo()
