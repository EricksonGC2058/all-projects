import time
import os

frameList = [
'''
   +---+
   O   |
  /|\\  |
  / \\  |
       |
       ==''','''
   +---+
  \\O/  |
   |   |
   \\\\  |
       |
       ==''','''
   +---+
       |
   \\O/ |
    |  |
   / \\ |
       ==''','''
   +---+
       |
       |
   \\O/ |
    |  |
    \\\\ ==''','''
   +---+
       |
       |
       |   ouch.
       |
  O/_//==''','''
   +---+
       |
       |
       |   ouch.
       |
  O____=='''
]

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.1)