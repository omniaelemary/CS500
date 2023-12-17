def add_and_subtract():
	num_1 = input("input first number: ")
	num_2 = input("input second number: ")
	
	addition = int(num_1)+int(num_2)
	subtraction = int(num_1)-int(num_2)
	
	print("The addition of these numbers is "+str(addition))
	print("The subtraction of these numbers is "+str(subtraction))
	
	return (addition, subtraction)
	
def multiply_and_divide():
	num_1 = input("input first number: ")
	num_2 = input("input second number: ")
	
	multiply = int(num_1)*int(num_2)
	divide = int(num_1)/int(num_2)
	
	print("The multiplication of these numbers is "+str(multiply))
	print("The division of these numbers is "+str(divide))
	
	return (multiply, divide)