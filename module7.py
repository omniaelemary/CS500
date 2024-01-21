def courses():
	
	#create dictionary for room number
	room_number = {
		"CSC101" : 3004,
		"CSC102" : 4501,
		"CSC103" : 6755,
		"NET110" : 1244,
		"COM241" : 1411
	}
	
	#create dictionary for instructors
	instructors = {
		"CSC101" : "Haynes",
		"CSC102" : "Alvarado",
		"CSC103" : "Rich",
		"NET110" : "Burke",
		"COM241" : "Lee"
	}
	
	#create dictionary for meeting times
	meeting_time = {
		"CSC101" : "8:00 a.m.",
		"CSC102" : "9:00 a.m.",
		"CSC103" : "10:00 a.m.",
		"NET110" : "11:00 a.m.",
		"COM241" : "1:00 p.m."
	}
	
	#ask user input for the course number
	course_number = input("Please enter a course number ")
	
	#try block to try to pull the info for the course user enters
	try:
		
		#access the dictionaries based on the user input
		#save info
		room = room_number[course_number]
		teacher = instructors[course_number]
		time = meeting_time[course_number]
		
		print("Your course room number is "+str(room))
		print("Your instructor is "+teacher)
		print("Your meeting time is "+time)
		
	#catch block, if user tries to enter info for course not in dictionary	
	except:
		print("I do not have information on the course you have entered")