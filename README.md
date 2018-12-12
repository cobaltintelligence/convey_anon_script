# convey_anon_script
Athlete data depersonalization utilities developed for Seann Convey

## Requirements
Python 3 or later.

## Usage
```
$ python app.py "<folder location>""
```

**Example**
```
$ python app.py "/Users/yuanwang/dev/convey_anon_script/data"
```
Which should produce
```
Location: /Users/yuanwang/dev/convey_anon_script/data

Renaming:
	CMJ_40106402_19APRIL2013.csv 	 --->  CMJ_2470413714_19APRIL2013.csv
	CMJ_48296536_16SEPTEMBER2013.csv 	 --->  CMJ_4930912758_16SEPTEMBER2013.csv

Saving lookup to lookup.csv

$ ls /Users/yuanwang/dev/convey_anon_script/data
	-  CMJ_4930912758_16SEPTEMBER2013.csv
	-  CMJ_2470413714_19APRIL2013.csv

Done
```

## Author
Yuan Wang, Graceland Research

## License
Copyright Cobalt Intelligence 2018. All rights reserved.