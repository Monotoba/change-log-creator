# CHANGELOG CREATOR

A tool for generating change log documents from Git Repositories.

Copyright 2022 Randall Morgan

## Introduction

This script can read the commit logs of a Git repository and 
extract data to produce changelogs in Markdown format.

## Usage

This script can be run from the commandline. The following 
commandline options are available:

#### Command-Line Options:

```
options:

  -h, --help            show this help message and exit
  
-r REPO, --repo REPO    The source repository
  
-b BRANCH, --branch BRANCH
                        The repository branch to query

-c COUNT, --count COUNT
                        The maximum number of commits to report

-o OUTFILE, --outfile OUTFILE
                        The file to save the Markdown into

-f, --force              Force output to overwrite existing file
```

A sample invocation to create a change log for a development branch:
```
$ change-log-creator -r ../ -b development -c 100 -o DEV_CHANGELOG.md -f
```

## API

If you wish to use change-log-creator as a module in your own 
document processor, the following text will help.

The module contains a single useful method as documented below.

```
create_change_log_from_repo(repo: str = None, branch: str = 'master', max_count=50):

    Creates a change log document in Markdown format.

    Parameters
    ----------
    repo: str
        The repository path
    branch: str
        The branch, defaults to "master"
    max_count: int
        The maximum number of commits to report

    Returns
    -------
        str
```


## License
This software is licensed under the GNU General Public License 
version 2 or later. At the user's discretion. You are free to
use this script, and it's source code any way you like. 

## Waranty
This software is provided without warranty of any kind! The user is 
solely responsibility to determine the suitability of this software 
for their own specific use case.
