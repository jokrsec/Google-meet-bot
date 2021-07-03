from config import TIMETABLE_PATH, ACADEMIC_YEAR, testing_start_time, testing_end_time
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
	"MOD": "https://meet.google.com/tof-wyre-qga"
}

class Period():
	def __init__(self, period, subject, starting_time, ending_time):
		self.period = period
		self.subject = subject
		self.starting_time = starting_time
		self.ending_time = ending_time



workbook = openpyxl.load_workbook(TIMETABLE_PATH)
sheet = workbook[ACADEMIC_YEAR]

# l = [col.value for col in sheet[7] if col.value!=None]

for col in sheet[6] + sheet[13]:
	if col.value != None and not col.value.startswith("BATCH") and not col.value.startswith("CSE"):
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


# adding test period
test_period = Period("P5", "MOD", testing_start_time, testing_end_time)
schedule_map['saturday'].append(test_period)

print("Testing class is scheduled at {} min from now with 2 minutes of running time..\n".format(testing_start_time))