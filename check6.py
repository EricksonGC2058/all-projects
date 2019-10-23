# Garrett Erickson
# Period 6

#variable Declaration and assignment
myVariable = "Erickson" # String variable
myNumber = 12 # int variable
myDecimal = 12.6 # float variable

# make a variable of type String
Poop = "How much u poo doe"

# while loops
x = 1
while x <= 10:
	print(x)
	x += 1
# make a while loop to count down from 100 to 1
x = 100
while x >= 1:
	print(x)
	x -= 1
# String concatenation
string1 = "Hello "
string2 = "world "
print(string1 + string2 + "!")

# make a variable with your favorite movie
favMovie = "Whiplash"
print("My favorite movie is " + favMovie)

# input
yourName = input("What is your name? ")
print("Hello " + yourName)

# prompt for favorite song
# print your favorite song is...
favSong = "Yo Mama Theme by Brody Foxx"
print("Your favorite song is " + favSong)

# casting - change one type to another (str to int)
myNum = input("Enter a number: ") #myNum is now a string type
myNum = int(myNum) + 10 # myNum is now an int
print("The answer is " + str(myNum))

# ask for two numbers, add them, and print the sum
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
myNum = int(num1) + int(num2)
print("Your answer is " + str(myNum))

# if and if/else
num = int(input("What is your number: "))

if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is 100")
else:
	print("Your number is less than 100")

# ask if today is your birthday
# if it is print Happy Birthday
bDay = input("Is today your birthday? ")
if bDay == "yes":
	print("Happy Birthday!")
if bDay == "no":
	print("It's not your birthday.")