#part 1
#calculate the total amount of a meal purchased at a restaurant 
def total_cost():
	
	#ask user to enter the charge for the food
	mealCost = input("How much was the charge for the food? ")
	
	try:
		#convert the meal cost to a float
		#round to only two decimal places
		mealCost = round(float(mealCost),2)
		
		#calculate 7% tax on the meal price
		#round to only two decimal places
		tax = round(mealCost * 0.07,2)
		
		#calculate 18% tip on the meal price
		#round to only two decimal places
		tip = round(mealCost * 0.18,2)
		
		#add meal cost, tax, and tip to get total cost
		#round to only two decimal places
		totalCost = round(mealCost + tax + tip,2)
		
		#print outcomes
		#make sure two decimal places are displayed even if one is a 0
		print("The tip for this meal is $"+"{:.2f}".format(tip))
		print("The tax for this meal is $"+"{:.2f}".format(tax))
		print("The total cost including tax and tip is $"+"{:.2f}".format(totalCost))
		
		#return the total cost
		return totalCost
		
	except: 
		#if the user enters a value that cannot be converted to float
		print("This is not a valid number, please try again")


#part 2
#be able to tell a user what time their alarm will go off
def clock():
	
	#ask user the time now (in hours)
	time = input("What is the time right now (in hours)? ")
	
	#ask user for number of hours to wait for the alarm
	alarmHours = input("How many hours do you want to wait for your alarm to go off? ")
	
	try:
		
		#convert user inputs to ints
		time = int(time)
		alarmHours = int(alarmHours)
		
		
		#add the numbers together to get how far ahead the alarm will be in
		#terms of the current time
		total = time + alarmHours
		
		
		#covert this time to be within 24 time frame
		#you get this by getting the remainder after dividing by 24
		userAlarm = total % 24
		
		#print result
		print("Your alarm will go off at "+str(userAlarm)+":00")
		
		#return result
		return userAlarm
		
	except: 
		#if the user enters values that cannot be converted to int
		print("This is not a valid number, please try again")
	
	