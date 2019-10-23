from turtle import *

turtleGame = Turtle()
myScreen = turtleGame.getscreen()
turtleGame.penup()
turtleGame.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/2-50)
turtleGame.hideturtle()
scoreNum = 0

def updateScore():
	turtleGame.clear()
	turtleGame.write("Score: " + str(scoreNum), False, "left", font=("Comic Sans MS", 20, "normal"))

updateScore()

myScreen.mainloop()