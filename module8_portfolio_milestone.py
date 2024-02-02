class ItemToPurchase:
    
    #this is a constructor for when params about item is provided
    #default values in order to simulate default constructor
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description="no description"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    #this is the printing function of the item costs 
    #this function also returns the total price based on quantity to later use in main function
    def print_item_cost(self):
        total_price = self.item_price * self.item_quantity
        print(self.item_name+ " "+str(self.item_quantity)+ " @ $"+str(self.item_price)+" = $"+str(total_price))
        return total_price
		
class ShoppingCart:
	
	#constructor that accepts customer name (str) and date (str) as paramaters
	#initialize cart as empty list
	#default values in order to simulate default constructor
	def __init__(self, customer_name = "none", date = "January 1, 2020"):
		self.customer_name = customer_name
		self.date = date
		self.cart_items = []
	
	#item is of class ItemToPurchase
	def add_item(self, item):
		#add item to the cart
		self.cart_items.append(item)
	
	#to remove items based on item name
	def remove_item(self, name_of_item):
		#go through cart
		for i in self.cart_items:
			#if you find item matching name 
			if i.item_name == name_of_item:
				#remove that item
				self.cart_items.remove(i)
				#return so you can exit out of the function
				return
		#if you never exit the function, it means you never found the item
		print("Item not found in cart")
		
	def modify_item(self, item):
		
		#check to make sure item given in param does not have default values
		if item.item_name!="none" and item.item_price!=0 and item.item_quantity!=0 and item.item_description!="no description":
			#search through cart
			for i in self.cart_items:
				#if a match is found based based on item name 
				if item.item_name == i.item_name:
					#update the item price
					i.item_price = item.item_price
					#update the item quantity
					i.item_quantity = item.item_quantity
					#update the item description
					i.item_description = item.item_description
					#exit the function
					return
			#if you never exit the function, it means you never found a match
			#let user know that there was no match found 
			print("Item not found in cart")
			
	#to change item quantity in shopping cart
	def change_quantity(self, item_name, new_quantity):
		#search through cart
		for i in self.cart_items:
			#if a match is found based based on item name 
			if item_name == i.item_name:
				#update the item quantity
				i.item_quantity = new_quantity
				#exit the function
				return
		#if you never exit the function, it means you never found a match
		#let user know that there was no match found 
		print("Item not found in cart")
	def get_num_items_in_cart(self):
		#create total_quantity var to keep track of items
		total_quantity = 0
		#go through cart
		for i in self.cart_items:
			#add each quantity to total quantities
			total_quantity += i.item_quantity
			
		#return the total
		return total_quantity
		
	def get_cost_of_cart(self):
		#create total_cost var to keep track of items
		total_cost = 0
		#go through cart
		for i in self.cart_items:
			#add each price to total price
			total_cost += i.item_price
			
		#return the total
		return total_cost
		
	def print_total(self):
		
		#if cart is empty
		if self.cart_items == []:
			#print required message
			print("SHOPPING CART IS EMPTY")
		else:
			#print the customer name and date
			print(self.customer_name+"'s Shopping Cart - "+self.date)
			#print how many items there are 
			print("Number of Items: "+str(self.get_num_items_in_cart()))
			#go through and print item cost for each item
			for i in self.cart_items:
				i.print_item_cost()
	
	#printing descriptions of items
	def print_descriptions(self):
		#if cart is empty
		if self.cart_items == []:
			#print required message
			print("SHOPPING CART IS EMPTY")
		else:
			#print the customer name and date
			print(self.customer_name+"'s Shopping Cart - "+self.date)
			#print out item description title
			print("Item Descriptions")
			#go through and print item description
			for i in self.cart_items:
				print(i.item_name+": "+i.item_description)
		
		
#this is the main function
def main_previous_milestones():
	
	#this is for the first item
	print("Item 1")
	
	#prompt user to enter info about first item
	item1_name = input("Enter the item name: \n")
	item1_description = input("Enter the item description: \n")
	item1_price = input("Enter the item price: \n")
	item1_quantity = input("Enter the item quanity: \n")
	
	#this is for the second item
	print("Item 2")
	
	#prompt user to enter info about second item
	item2_name = input("Enter the item name: \n")
	item2_description = input("Enter the item description: \n")
	item2_price = input("Enter the item price: \n")
	item2_quantity = input("Enter the item quanity: \n")
	
	#create the item to purchase objects with all the info given from user and convert to correct type
	itemToPurchase1 = ItemToPurchase(item1_name, float(item1_price), int(item1_quantity), item1_description)
	itemToPurchase2 = ItemToPurchase(item2_name, float(item2_price), int(item2_quantity), item2_description)
	
	#this prints a summart of total costs
	print("TOTAL COST")
	
	#get the total costs from the class objects
	total1 = itemToPurchase1.print_item_cost()
	total2 = itemToPurchase2.print_item_cost()
	
	#add up both totals
	totals = total1 + total2
	
	#return the grand total of both class objects
	print("Total: $"+str(totals))
	
def main():
	name = input("Enter customer's name: \n")
	date = input("Enter today's date: \n")
	new_shopping_cart = ShoppingCart(name, date)
	print_menu(new_shopping_cart)
	
	
def print_menu(shopping_cart):
	
	#create a var to keep track if you need to keep printing menu and asking user choice
	keep_asking = True 
	
	#start a while loop that will keep going until user quits
	while keep_asking:
		#print out the menu
		print("MENU")
		print("a - add item to cart")
		print("r - remove item from cart")
		print("c - Change item quantity")
		print("i - Output items' descriptions")
		print("o - Output shopping cart")
		print("q - Quit")
		#ask user for their input
		user_choice = input("Choose an option: ")
		
		#user wants to quit
		if user_choice == 'q':
			#you don't need to keep asking anymore
			keep_asking = False
			#exit the function
			return
		#user wants to remove item
		elif user_choice == 'r':
			#ask user for the name of the item
			item_name = input("what is the name of the item? ")
			#remove item from shopping cart
			shopping_cart.remove_item(item_name)
		#user want to modify item
		elif user_choice == 'c':
			#prompt user to enter info about item it wants to modify
			item1_name = input("Enter the item name: \n")
			#prompt user for new quanitity
			item1_quantity = input("Enter new item quanity: \n")
			#call change quantity function
			shopping_cart.change_quantity(item1_name, int(item1_quantity))
		#user want to output all descriptions
		elif user_choice == 'i':
			print("OUTPUT ITEMS' DESCRIPTIONS")
			#call print descriptions function on shopping cart
			shopping_cart.print_descriptions()
		#user wants to output shopping cart
		elif user_choice == 'o':
			print("OUTPUT SHOPPING CART")
			#call the print total function
			shopping_cart.print_total()
		#add item to cart
		elif user_choice == 'a':
			#prompt user to enter info about new item
			item1_name = input("Enter the item name: \n")
			item1_description = input("Enter the item description: \n")
			item1_price = input("Enter the item price: \n")
			item1_quantity = input("Enter the item quanity: \n")
			#create new item object to be modify in shopping cart
			new_item = ItemToPurchase(item1_name, float(item1_price), int(item1_quantity), item1_description)
			#add new item to shopping cart
			shopping_cart.add_item(new_item) 
		#if user tries to ask for option not on menu
		else:
			print("that is not a valid choice")

#this is to execute main function
if __name__ == "__main__":
	main()