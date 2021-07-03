# Google-meet-bot
An automation tool which is useful to attend your online class.

## What it does?
- It takes a timetable.
- Attends online classes whole day without your interaction.
- It just sleeps when there are no classes.
- Just configure and run it. It will do it's work
- Timetable parser is only available for RGUKTNs as of now. I will add a generic way in next update


## Configuration

### Add following pairs to your config file (config.py)
```
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

### Files required
- Rename your timetable (excel file) to __timetable.xlsx__ and add it to root folder of project.
- Add geckodriver (FireFox WebDriver) executable to the root folder of project.

### Add meetlinks 
__make sure you add meet links appropriate to your subjects__ at line 37 in **update_timetable.py** like shown below:


### How to run the program:
- You can run the program once and leave it. It will do it's work
- You can run the program using python3

- Use the following commands to run the program:

### Testing locally 
- Add the below lines at end of config.py and run the program
```
#testing a class with is scheduled at 2 min after program starts

DEV = 1
from datetime import datetime, timedelta

# host a google meet, add the meating link for testing
testing_meet_link = "https://meet.google.com/nsf-wzzn-vnh"

testing_start_time = datetime.now() + timedelta(minutes=2)
testing_end_time = testing_start_time + timedelta(minutes=1)


testing_start_time = testing_start_time.strftime(TIME_FORMAT)
testing_end_time = testing_end_time.strftime(TIME_FORMAT)

```

```
pip install -r requirements.txt
python app.py
```

### Further updates: 

- Add notification system to notify you when the bot joins or leaves the class
- Store a custom timetable which can be used to schedule classes for NON-RGUKTNs

