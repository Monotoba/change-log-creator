#!/usr/bin/env python3

import argparse
from git.exc import GitError

from change_log_creator.change_log_creator import create_change_log_from_repo


def main(argv=None):
    parser = argparse.ArgumentParser(prog="change-log-creator")

    parser.add_argument("-r", "--repo", help="The source repository", type=str, required=True)
    parser.add_argument("-b", "--branch", help="The repository branch to query", type=str, required=False)
    parser.add_argument("-c", "--count", help="The maximum number of commits to report\n", type=int, required=False)
    parser.add_argument("-o", "--outfile", help="The file to save the Markdown into\n", required=False)
    parser.add_argument("-f", "--force", help="Force output to overwrite existing file", action="store_true", required=False)

    args = parser.parse_args(argv)

    # Get command params or use defaults
    repo = args.repo
    branch = args.branch
    count = args.count if args.count is not None else 50

    # Get markdown
    try:
        text = create_change_log_from_repo(repo=repo, branch=branch, max_count=count)
    except (GitError, OSError, ValueError) as exc:
        parser.error(str(exc))

    # Exclusive creation prevents overwriting an existing file without --force.
    if args.outfile is not None:
        try:
            with open(args.outfile, "w" if args.force else "x", encoding="utf-8") as fho:
                fho.write(text)
        except FileExistsError:
            parser.error("Output file already exists; use --force (-f) to overwrite it")
        except OSError as exc:
            parser.error(str(exc))
    else:
        print(text)


if __name__ == '__main__':
    main()
