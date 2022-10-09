
import turtle
pen = turtle.Turtle()
def curve():
	for i in range(200):
    
		pen.right(1)
		pen.forward(1)

def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('lightgreen')

	pen.write("ABESEC", font=(
	"Verdana", 12, "bold"))


heart()
txt()
pen.ht()
