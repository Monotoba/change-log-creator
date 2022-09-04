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



## API

If you wish to use change-log-creator as a module in your own 
document processor, the following text will help.

``` { .python replace }

from change_log_creator.change_log_creator import create_change_log_from_repo
from npdoc_to_md import render_obj_docstring

print(render_obj_docstring(obj='create_change_log_from_repo'))

```

## License
This software is licensed under the GNU General Public License 
version 2 or later. At the user's discretion. You are free to
use this script, and it's source code any way you like. 

## Waranty
This software is provided without warranty of any kind! The user is 
solely responsibility to determine the suitability of this software 
for their own specific use case.


``` { .python replace }
#from change_log_creator.change_log_creator.change_log_creator import create_change_log_from_repo
#output = create_change_log_from_repo(repo='../', branch='master')
```
