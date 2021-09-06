from googleapiclient.discovery import build
import pickle, datetime, os.path

def main():

	creds = None

	if os.path.exists('token.pickle'):				#checks for and uses the authentication token already made in quickstart.py
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)

	if not creds or not creds.valid:				#refreshes token if expired. if the token is invalid the program exits
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			exit()

	service = build('calendar', 'v3', credentials=creds)
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	#gets the first 30 events on the calander
	events_result = service.events().list(calendarId='primary', timeMin=now,
										maxResults=30, singleEvents=True,
										orderBy='startTime').execute()

	events = events_result.get('items', [])
	#loops through the events returned
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date')) # start date and time
		end = event['end'].get('dateTime', event['end'].get('date'))	   # end date and time
		try:
			if(event['summary'].index("Hotschedules") > -1):    #checks if the event is a hot schedules event
				startHour = int(start[11] + start[12] + "")		#gets the start time as an integer ("" forces it to concatinate and not add)
				endHour = int(end[11] + end[12] + "")			#gets the end time as an integer 
				if (endHour - startHour  < 2):					#checks if the time needs to be changed
					newEndTime = endHour + 5
					newEndDT=""
					if (startHour  < 15):						#checks if its a morning shift, and ends the shift at 3:30
						newEndDT = end[:11] + "15:30" +end[15:] # takes the datetime string from google and replaces the time with the end time of a morning weekend shift 
					else:										#sets the ent of the shift to 5 hours after it starts
						newEndDT = end[:11] + str(newEndTime) + end[13:] # takes the exact string from google and replaces the end time with the updated end time
					print("old DT :" +str(event['end']))
					event['end'] = eval("{'dateTime': '" + newEndDT + "'}")
					print("new DT :" +str(event['end']))
					updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
					print("Event update Succesful!")
		except ValueError: 
			0

if __name__ == '__main__':
	main()