# Change Log Creator

[![Tests](https://github.com/Monotoba/change-log-creator/actions/workflows/tests.yml/badge.svg)](https://github.com/Monotoba/change-log-creator/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
[![License](https://img.shields.io/badge/License-BSD--2--Clause-blue)](LICENSE)

Generate a Markdown commit-history report from a local Git repository. Use it to
review recent work or prepare a changelog draft for a branch or revision.
Each entry contains the commit message, committer identity, authored timestamp,
and author timezone offset. This is a raw history report, not a curated release-note generator.

## Install

Requires Python 3.10+ and Git on PATH. From a terminal:

```sh
git clone https://github.com/Monotoba/change-log-creator.git
cd change-log-creator
python -m venv .venv
# Linux/macOS:
. .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1
python -m pip install .
change-log-creator --help
```

## Generate a report

```sh
change-log-creator -r ../my-project -c 20
change-log-creator -r ../my-project -b development -c 100 -o DEV_CHANGELOG.md
```

| Option | Meaning |
|---|---|
| `-r`, `--repo` | Required local Git repository path; `~` is expanded |
| `-b`, `--branch` | Branch or revision; defaults to current `HEAD` |
| `-c`, `--count` | Positive maximum commit count; defaults to 50 |
| `-o`, `--outfile` | UTF-8 Markdown output path; defaults to standard output |
| `-f`, `--force` | Permit overwriting an existing output file |

Without `--force`, an existing output file is preserved and the command fails.
Invalid repositories, revisions, or counts produce command-line errors.
The original launcher remains available as `python change-log-creator.py ...`.

## Python API

```python
from change_log_creator.change_log_creator import create_change_log_from_repo

markdown = create_change_log_from_repo(
    repo="../my-project", max_count=20, branch="HEAD"
)
```

The API returns a string and raises exceptions for invalid inputs. It does not
write output files. Omitting `branch` uses the current HEAD, including repositories
whose default branch is `main`. An empty repository has no history to report.

## Validation and contributions

```sh
python -m pip install -e .
python -m unittest discover -s tests -v
```

Tests create real temporary Git repositories and check branch/count selection,
CLI errors, output generation, and overwrite protection. CI tests Linux, macOS,
and Windows, builds wheel/source packages, and checks the installed wheel command
outside the checkout. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Limitations

Commit messages are included verbatim in Markdown code fences; embedded fences may
need editing before publication. Output timestamps use local time, and report dates
change between runs. Committer identity may differ from the commit author. Reports
can contain names, email addresses, or sensitive commit messages: review before sharing.

## License

[BSD-2-Clause](LICENSE), copyright 2022 Randall Morgan. Retain the copyright notice
and license terms when redistributing. Provided without warranty under the license.
