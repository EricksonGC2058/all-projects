print("Welcome to the To Do List! (:")
todolist = []
while True:
	print("Enter 'a' to add an item")
	print("Enter 'r' to remove an item")
	print("Enter 'p' to print the list")
	print("Enter 'q' to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		todoitems = input("What will you add to your list? ")
		todolist.append(todoitems)
	elif choice == "r":
		todotakeout = input("What will you take out of your list? ")
		todolist.remove(todotakeout)
	elif choice == "p":
		count = 1
		for todoitems in todolist:
			print("Task " + str(count) + ": " + todoitems)
			count = count + 1
	else:
		print("That is not a choice, please try again.")