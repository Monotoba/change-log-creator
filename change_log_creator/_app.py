#!/usr/bin/env python3

import argparse
import os

from change_log_creator.change_log_creator import create_change_log_from_repo


def main():
    usage_msg = ""

    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser(usage=usage_msg, prog="changelog-creator")

    parser.add_argument("-r", "--repo", help="The source repository", type=str, required=True)
    parser.add_argument("-b", "--branch", help="The repository branch to query", type=str, required=False)
    parser.add_argument("-c", "--count", help="The maximum number of commits to report\n", type=int, required=False)
    parser.add_argument("-o", "--outfile", help="The file to save the Markdown into\n", required=False)
    parser.add_argument("-f", "--force", help="Force output to overwrite existing file", action="store_true", required=False)

    args = parser.parse_args()

    # Get command params or use defaults
    repo = args.repo
    branch = args.branch if args.branch is not None else 'master'
    count = args.count if args.count is not None else 50

    # Get markdown
    text = create_change_log_from_repo(repo=repo)

    # Save to output file
    if args.outfile is not None:
        if os.path.isfile(args.outfile) and not args.force:
            raise ValueError(
                f"Error: {args.outfile} file already exist! Use the --force (-f) flag to force overwriting existing files.")

    if args.outfile is not None:
        with open(args.outfile, 'w') as fho:
            fho.write(text)
    else:
        print(text)


if __name__ == '__main__':
    main()
