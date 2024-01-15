#part 1

def rainfall():
	
	#keep track of all the inches of rainfall
	total_rainfall=0
	
	#ask user for number of years
	num_of_years = input("How many years do you want to calculate the average rainfall for? ")
	
	try:
	
		#outer loop iterates for num of years
		for i in range(0,int(num_of_years)):
			
			#inner loop iterates for num of months in the year
			for j in range(0,12):
				
				#ask user for current rainfall that month
				curr_rainfall = input("How many inches of rainfall in month "+str(j+1)+" in year "+str(i+1)+"? ")
				
				#add rainfall of the month to total rainfall
				total_rainfall += int(curr_rainfall)
				
		#calculate the average rainfall per month during the period
		average_rainfall = total_rainfall / (int(num_of_years) * 12)
		
		#calculate total number of months
		num_of_months = int(num_of_years) * 12
		
		#print out results
		print("There were "+str(num_of_months)+" months during this period")
		print("There were a total "+str(total_rainfall)+" inches of rainfall during this period")
		print("There was an average rainfall of "+str(average_rainfall)+" inches per month")
		
	
	#catch block in case the user inputs something that cannot be converted to int
	except:
		print("This is not a valid input, please input an int")
		
#part 2
def awardPoints():
	
	try:
		#ask users for how many books they purchased
		books = input("How many books did you purchase this month? ")
		
		#less than 2 books (0 or 1)
		if int(books)<2:
			print("You have earned 0 points")
		#2 or more books but less than 4 (2 or 3)
		elif int(books)>=2 and int(books)<4:
			print("You have earned 5 points")
		#4 or more books but less than 6 (4 or 5)
		elif int(books)>=4 and int(books)<6:
			print("You have earned 15 points")
		#6 or more books but less than 8 (6 or 7)
		elif int(books)>=6 and int(books)<8:
			print("You have earned 30 points")
		#for 8 or more books
		else:
			print("You have earned 60 points")
			
			
		
	#catch block incase user does not enter in an int
	except:
		print("This is not a valid input, please input an int")