from pages import GoogleLoginPage, JoinMeet
import schedule
import time
from datetime import datetime
from update_timetable import schedule_map, location_map
from config import *
from time import sleep

def get_day():
	return datetime.today().strftime("%A").lower()

def get_period_number():
	current_time = datetime.now().strftime(TIME_FORMAT)
	if current_time >= "10:00" and current_time <= "11:00":
		return 0
	elif current_time >= "11:30" and current_time <= "12:30":
		return 1
	elif current_time >= "15:00" and current_time <= "16:00":
		return 2
	elif current_time >= "16:30" and current_time <= "17:30":
		return 3
	elif current_time >= testing_start_time and current_time <= testing_end_time:
		return 3
	else:
		return -1

def schedule_logout(class_running_time, meet_page):

	l = list(map(int, class_running_time.split(':')))
	hours, minutes = l[0], l[1]
	class_running_time = (int(hours) * 60) + int(minutes)

	print("[+] Scheduled logout after {} minte(s)".format(class_running_time))
	sleep(class_running_time * 60)
	meet_page.leave()

def join(location, subject, starting_time, ending_time):

	class_running_time = datetime.strptime(ending_time, TIME_FORMAT) - datetime.strptime(starting_time, TIME_FORMAT)

	google_page = GoogleLoginPage()
	google_page.login()

	meet_page = JoinMeet()
	meet_page.join(location)
	print("[+] Joined the class")

	schedule_logout(str(class_running_time), meet_page)

def take_break(break_type):

	start_time = ""
	end_time = ""

	if break_type == "lunch":
		print("[+] It's your lunch time.")
		start_time = LUNCH_BREAK_START_TIME
		end_time = LUNCH_BREAK_END_TIME

	elif break_type == "sleep":
		print("[+] Time to stay away from classes.")
		start_time = SLEEP_START_TIME
		end_time = SLEEP_END_TIME

	else:
		print("[+] Yaay! Its sunday.")
		start_time = CLASS_START_TIME
		end_time = CLASS_END_TIME

	break_time = datetime.strptime(end_time, TIME_FORMAT) - datetime.strptime(start_time, TIME_FORMAT)
	l = list(map(int, break_time.split(':')))
	hours, minutes = l[0], l[1]
	break_time = (int(hours) * 60) + int(minutes)

	sleep(break_time * 60)

def check_for_class():
	day = get_day()

	if day == "sunday":
		take_break("sunday")
		return

	period_number = get_period_number()

	if period_number == -1:
		print("[-] No class at this time!")
		return

	print("\n[+] Class is available")

	try:
		period = schedule_map[day][period_number]
	except:
		period = schedule_map[day][period_number-1]

	subject = period.subject
	starting_time = period.starting_time
	ending_time = period.ending_time

	try:
		location = location_map[subject]
	except:
		print("Add meating links for all subjects.")
		exit()

	print("\nFetching class details..")

	print("Period: ", period.period)
	print("Subject: ", subject)
	print("Start time: ", starting_time)
	print("End time: ", ending_time)
	print("Meeting link: ", location)
	print()
 
	trail = 0
	while trail<=15:
		try:
			print("[+] Trying to attend the class..")
			join(location, subject, starting_time, ending_time)
			break
		except:
			sleep(60)

		trail += 1

	else:
		print("Tutor is not available!. Waiting for next class")
		sleep(30*60)



def run_schedule():

	print("[+] Schedule initiated.")
	print("[+] Waiting for classes..")

	schedule.every().day.at("10:00").do(check_for_class)
	schedule.every().day.at("11:30").do(check_for_class)
	schedule.every().day.at("15:00").do(check_for_class)
	schedule.every().day.at("16:30").do(check_for_class)
	schedule.every().day.at("12:35").do(take_break, "lunch")
	schedule.every().day.at("17:40").do(take_break, "sleep")

	if DEV == 1:
		print("Testing class is scheduled at {} min from now with 1 minute of running time..\n".format(testing_start_time))
		schedule.every().day.at(testing_start_time).do(check_for_class)


	while True:
	    schedule.run_pending()
    

if __name__=="__main__":
	run_schedule()


