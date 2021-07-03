# Google Meet Bot (online classes, duh!)
An automation tool which is useful to attend your online classes forever without your interaction.

## What it does?
- It takes a timetable.
- Attends online classes whole day without your interaction.
- It just sleeps when there are no classes.
- Just configure and run it. It will do it's work
- Timetable parser is only available for RGUKTNs as of now. I will add a generic way in next update


## Configuration

### Add following pairs to your config file (config.py)
```python
GOOGLE_LOGIN_SERVICE = "https://accounts.google.com/servicelogin"
GMAIL_IDENTIFIER = <your_gmail or phone_number>;
GMAIL_PASSWORD = <your_gmail_password>;

# Below configuration is only for RGUKTNs

TIMETABLE_PATH = "./timetable.xlsx"
ACADEMIC_YEAR = "E2"
BRANCH = "CSE"  # Ex: ECE, CIV
BATCH_NO = 3

TIME_FORMAT = "%H:%M"

LUNCH_BREAK_START_TIME = "12:35" 
LUNCH_BREAK_END_TIME = "14:45"

SLEEP_START_TIME = "17:40"
SLEEP_END_TIME = "09:45"

CLASS_START_TIME = "10:00"
CLASS_END_TIME = "17:30"
```
- create a file named _config.py_ in root folder of project

### Files required
- Rename your timetable (excel file) to __timetable.xlsx__ and add it to root folder of project.
- Project requires a webdriver to run. You can download one at 
- [geckodriver for linux64](https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz)
- [geckodriver for win64](https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip)
- You can find driver for other platforms at [here](https://github.com/mozilla/geckodriver/releases)
- Extract and add geckodriver (FireFox WebDriver) executable to the root folder of project.

### Add meetlinks 
- _make sure you add meet links appropriate to your subjects_ at line 37 in **update_timetable.py** like shown below:

```python
location_map = {
	"DBMS": "https://meet.google.com/jwp-xofc-ykn",
	"FLAT": "https://meet.google.com/lookup/djfgl425yy?authuser=0&hs=179",
	"WT": "https://meet.google.com/lookup/eejnnklktc?authuser=0&hs=179",
	"OR": "https://meet.google.com/lookup/ednwftrdtp?authuser=0&hs=179",
	"COA": "https://meet.google.com/lookup/cnynyohxn7?authuser=0&hs=179",
	"Eng-ll": "https://meet.google.com/lookup/eejnnklktc?authuser=0&hs=179",
	"DBMSL" : "https://meet.google.com/lookup/eeo6ddnvqu?authuser=0&hs=179",
	"COAL": "https://meet.google.com/lookup/dw2m6w2nlt?authuser=0&hs=179",
	"WTL": "https://meet.google.com/lookup/eejnnklktc?authuser=0&hs=179",
	"TEST": testing_meet_link

}
```

### How to run the program?
- You can run the program once and leave it. It will do it's work
- You can run the program using python3
```python
pip install -r requirements.txt
python app.py
```

- Use the following commands to run the program:

### Testing locally 
- Add the below lines at end of config.py and run the program
```python
#testing a class with is scheduled at 2 min after program starts

DEV = 1
from datetime import datetime, timedelta

# host a google meet, add the meating link for testing
testing_meet_link = "https://meet.google.com/nsf-wzzn-vnh" # replace this link

testing_start_time = datetime.now() + timedelta(minutes=2)
testing_end_time = testing_start_time + timedelta(minutes=1)


testing_start_time = testing_start_time.strftime(TIME_FORMAT)
testing_end_time = testing_end_time.strftime(TIME_FORMAT)
```
- Host a google meet and use it as a testing_meet_link

### Further updates

- Add notification system to notify you when the bot joins or leaves the class
- Store a custom timetable which can be used to schedule classes for NON-RGUKTNs

