myClasses = ["Algebra", "English", "Government"]
print(myClasses)

# add an item to the list
# append or insert
# append will add to the back of the list
myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorite class? ")
myClasses.append(favClass)
print(myClasses)
# insert
myClasses.insert(3, "Graphic Design")
print(myClasses)
# overwrite
myClasses[4] = "Journalism"
print(myClasses)

# remove list items
# remove, pop
# remove will remove a specific item
myClasses.remove("Journalism")
print(myClasses)
# myClasses.remove("Lunch")
# pop will remove an item at a specific index\
myClasses.pop() # erases the last item
print(myClasses)
myClasses.pop(1)
print(myClasses)
# len - returns the length of a list
print("myClasses is " + str(len(myClasses)) + " items long")

print(myClasses[len(myClasses) - 1])

# loop through a list
count = 1
for aClass in myClasses:
	print("Item " + str(count) + " is " + aClass)
	count = count + 1

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
total = 0
for aNum in numbers:
	total = total + aNum
print(total)

myClasses.append("cooking")
if "cooking" in myClasses:
	print("Have fun cooking")
else:
	print("ok... :(")
