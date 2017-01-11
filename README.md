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
