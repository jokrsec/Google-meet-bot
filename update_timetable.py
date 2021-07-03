from config import *
import openpyxl

schedule_map = {
	'monday': [],
	'tuesday': [],
	'wednesday': [],
	'thursday': [],
	'friday': [],
	'saturday': []
}

period_map = {
	3: "P1",
	4: "P2",
	6: "P3",
	7: "P4",
	8: "P1",
	9: "P2",
	11: "P3",
	12: "P4",
	13: "P1",
	14: "P2",
	16: "P3",
	17: "P4"

}

timing_map = {
	"P1": { "starting_time": "10:00", "ending_time": "11:00" },
	"P2": { "starting_time": "11:30", "ending_time": "12:30" },
	"P3": { "starting_time": "15:00", "ending_time": "16:00" },
	"P4": { "starting_time": "16:30", "ending_time": "17:30" },
	
}

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

def get_batch_row(batch_no):

	if batch_no < 1 and batch_no > 4:
		print("Batch number is out of bounds (1-4).")
		exit()

	row1 = batch_no + 3
	row2 = batch_no + 10
	return (row1, row2)

def configure_excel():
	try:
		workbook = openpyxl.load_workbook(TIMETABLE_PATH)
	except FileNotFoundError:
		print("Timetable not found!")

	if ACADEMIC_YEAR not in ["E1", "E2", "E3", "E4"]:
		print("Invalid academic year!")
		exit()
	return workbook[ACADEMIC_YEAR]
	


class Period():
	def __init__(self, period, subject, starting_time, ending_time):
		self.period = period
		self.subject = subject
		self.starting_time = starting_time
		self.ending_time = ending_time



sheet = configure_excel()
row1, row2 = get_batch_row(BATCH_NO)

for col in sheet[row1] + sheet[row2]:
	if col.value != None and not col.value.startswith("BATCH") and not col.value.startswith(BRANCH):
		try:
			subject = col.value
			period = period_map[col.column]
			starting_time = timing_map[period]["starting_time"]
			ending_time = timing_map[period]["ending_time"]

			period_object = Period(period, subject, starting_time, ending_time)

			if col.row < 8:

				if col.column >= 3 and col.column < 8:
					schedule_map['monday'].append(period_object)
				elif col.column >= 8 and col.column < 13:
					schedule_map['tuesday'].append(period_object)
				else:
					schedule_map['wednesday'].append(period_object)

			else:

				if col.column >= 3 and col.column < 8:
					schedule_map['thursday'].append(period_object)
				elif col.column >= 8 and col.column < 13:
					schedule_map['friday'].append(period_object)
				else:
					schedule_map['saturday'].append(period_object)
		except:
			pass


# adding test period, comment the below code for production
test_period = Period("P5", "TEST", testing_start_time, testing_end_time)
schedule_map['saturday'].append(test_period)

