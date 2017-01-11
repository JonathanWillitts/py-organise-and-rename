# Python Organise By Year and Rename
[![Build Status](https://travis-ci.org/JonathanWillitts/py-organise-and-rename.svg?branch=master)](https://travis-ci.org/JonathanWillitts/py-organise-and-rename)  


## Overview
Script/module to traverse a given directory, organise (by year) and rename any 'yymmdd' prefixed subdirectories to begin in the format: 'YYYY-mm-dd'.

e.g. given the following directory as the root:
```
├───000000 - Non date
├───010506 - A while ago
├───101225 - Christmas 2010
├───160120 Last January
├───170109_Yesterday
├───170110 - Today
├───Folder not to touch
└───_folder
```

the script would organise and rename the directories as follows:

```
├───000000 - Non date
├───2001
│   └───2001-05-06 - A while ago
├───2010
│   └───2010-12-25 - Christmas 2010
├───2016
│   └───2016-01-20 Last January
├───2017
│   ├───2017-01-09_Yesterday
│   └───2017-01-10 - Today
├───Folder not to touch
└───_folder

```

## Install & Run
First download the repository:

    git clone https://github.com/JonathanWillitts/py-organise-and-rename.git

Next edit the `config.ini` config file, specifying the (required) root directory, and (optional) log file path:
```
[MISC]
# (Required) Root directory whose subdirectories are to be organised and renamed.
root_directory = full/unquoted/path/to/root/dir/to/check

# (Optional) File path to save log file to.
# Set blank to disable file logging (and only log to console).
log_file = full/unquoted/path/to/to/store/log/file/organise_and_rename.log
```

Finally run the script, e.g.:

    python organise_by_year_and_rename.py

To get output as follows:
```
[2017-01-10 07:28:47,544] INFO     Logging to log file: test_dir/organise_and_rename.log
[2017-01-10 07:28:47,545] INFO     
---
Checking directories in: 'test_dir'
---
[2017-01-10 07:28:47,568] WARNING  Skipping folder '000000 - Non date' as it does not start in format 'yymmdd'. Exception details: time data '000000' does not match format '%y%m%d'
[2017-01-10 07:28:47,568] INFO     Moving 'test_dir\010506 - A while ago' to 'test_dir\2001\2001-05-06 - A while ago'
[2017-01-10 07:28:47,576] INFO     Moving 'test_dir\101225 - Christmas 2010' to 'test_dir\2010\2010-12-25 - Christmas 2010'
[2017-01-10 07:28:47,583] INFO     Moving 'test_dir\160120 Last January' to 'test_dir\2016\2016-01-20 Last January'
[2017-01-10 07:28:47,594] INFO     Moving 'test_dir\170109_Yesterday' to 'test_dir\2017\2017-01-09_Yesterday'
[2017-01-10 07:28:47,641] INFO     Moving 'test_dir\170110 - Today' to 'test_dir\2017\2017-01-10 - Today'
```

## CI Build
At present just checks that the code passes Pylint and Flake8 checks without errors/warnings.

## Platform
Developed and tested using Python 3.5 on Windows 7/10.  Not tested on Linux, though I see no obvious reason why it wouldn't work.

## Real world usage
Ran successfully on my own 'Pictures' folder containing 22,935 image files under 468 folders.
