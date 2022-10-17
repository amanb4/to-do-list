user_input = 'random'

data = list()


def showMenu():
	print("Menu:")
	print("1. Add an item:")
	print("2. Mark as Done:")
	print("3. View Items:")
	print("4. Exit:")


while user_input != '4':

	showMenu()
	user_input = input("Enter Your Choice: ")

	if user_input == '1':
		item = input("What is to be done ? ")
		data.append(item)
		print("Added item:", item)
	elif user_input == '2':
		item = input("What is to be marked as Done ")


		if item in data:
			data.remove(item)
			print("Removed item:", item)
		else:
		    print("Item does not exist in the to-do list ")
	elif user_input == '3':
		print("List of TO-DO Items: ")
		for items in data:
			print(items)
	    
	elif user_input == '4':
	    print("Good Bye")  