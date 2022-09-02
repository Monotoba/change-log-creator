from git import Repo

def create_change_log_from_repo(repo: str=None, max_count=50):

    if repo is not None:
        raise ValueError('A repository must be supplied!')

    local_repo = Repo(repo)

    commits = local_repo.iter_commits('origin', max_count=max_count)

    output = ''
    for commit in commits:
        print(commit.authored_datetime)
        print(commit.message)
        print(commit.author)
        print(commit.author_tz_offset)


if __name__ == '__main__':
    repor = '~/projects/python-3/change-log-creator'
    create_change_log_from_repo()
