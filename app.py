from pages import GoogleLoginPage, JoinMeet
import schedule
import time
from datetime import datetime
from update_timetable import schedule_map, location_map
from config import TIME_FORMAT, testing_start_time, testing_end_time
from time import sleep

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

	print("[+] Scheduled logout after {} mintes".format(class_running_time))
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


def check_for_class():
	day = datetime.today().strftime("%A").lower()
	period_number = get_period_number()

	if period_number == -1:
		print("[-] No class at this time!")
		return

	print("\n[+] Class is available")

	period = schedule_map[day][period_number]
	subject = period.subject
	starting_time = period.starting_time
	ending_time = period.ending_time

	location = location_map[subject]

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
		print("Tutor is not available!")

def run_schedule():

	print("[+] Schedule initiated.")

	schedule.every().day.at("10:00").do(check_for_class)
	schedule.every().day.at("11:30").do(check_for_class)
	schedule.every().day.at("15:00").do(check_for_class)
	schedule.every().day.at("16:30").do(check_for_class)
	schedule.every().day.at(testing_start_time).do(check_for_class)


	while True:
	    schedule.run_pending()
    

if __name__=="__main__":
	run_schedule()


