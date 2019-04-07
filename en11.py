import turtle 

t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(0, -600)
t.pendown()

total = 126
angle = total/18
start = (180+total)/2

t.left(start)

row, col = [], []
front_row = []

t.pencolor("white")
t.forward(600)
t.pencolor("black")
row.append(t.position())
step = 50
for _ in range(8):
	t.forward(step)
	row.append(t.position())
t.pencolor("white")
t.forward(step)
row.append(t.position())

# To draw rows
radius = 600
row_angle = 64.5
for i in range(10):
	t.up()
	t.goto(row[i][0], row[i][1])
	t.down()
	t.setheading(65)

	t.pencolor("white" if i == 9 else "black")
	col.append(t.position())
	t.circle(-radius, angle)	#1
	col.append(t.position())
	t.circle(-radius, angle)	
	col.append(t.position())
	t.circle(-radius, angle)	
	col.append(t.position())

	t.pencolor("white")
	t.circle(-radius, angle)
	col.append(t.position())
	if i < 4:
		front_row.append((t.position(), t.heading()))

	t.pencolor("white" if i <= 3 else "black")
	t.circle(-radius, angle)	#2
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())

	t.pencolor("white")
	t.circle(-radius, angle)
	col.append(t.position())

	t.pencolor("white" if i <= 3 else "black")
	t.circle(-radius, angle*2)	#3
	col.append(t.position())

	t.pencolor("white")
	t.circle(-radius, angle)
	col.append(t.position())

	t.pencolor("white" if i <= 3 else "black")
	t.circle(-radius, angle)	#4
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())

	t.pencolor("white")
	t.circle(-radius, angle)
	col.append(t.position())

	t.pencolor("white" if i == 9 else "black")			#5
	t.circle(-radius, angle)
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())
	t.circle(-radius, angle)
	col.append(t.position())

	radius += 50

del col[18:]

# To draw columns
t.pencolor("black")
for i in range(18):
	t.up()
	t.goto(col[i][0], col[i][1])
	t.down()
	t.setheading(start-i*7 if i <= 8 else start-i*7-5)
	if i >= 4 and i <= 13:
		t.pencolor("white")
		t.forward(step*4+5)
		t.pencolor("black")
	t.forward(5*step+5 if i >= 4 and i <= 13 else 408)

# To draw front row
front_col = []
radius = 600
for i in range(4):
	t.up()
	t.goto(front_row[i][0][0], front_row[i][0][1])
	t.down()
	t.setheading(front_row[i][1])
	if i == 0:
		front_col.append(t.position())
		for _ in range(3):
			t.circle(-radius, angle*10/3)
			front_col.append(t.position())
	elif i == 2:
		for _ in range(5):
			t.circle(-radius, angle*2)
			front_col.append(t.position())
	else:
		t.circle(-radius, angle*10)
	radius += 50

# To draw front column
t.up()
t.goto(front_col[0][0], front_col[0][1])
t.down()
start_angle = start - 4*7
t.setheading(start_angle)
t.forward(step*3)
ind = 1
for i in range(2):
	t.up()
	t.goto(front_col[ind][0], front_col[ind][1])
	t.down()
	t.setheading(start_angle - 7*10*(i+1)/3)
	t.forward(2*step)
	ind += 1
t.up()
t.goto(front_col[ind][0], front_col[ind][1])
t.down()
t.setheading(start_angle-10*7)
t.forward(step*3+5)
ind += 1
for i in range(4):
	t.up()
	t.goto(front_col[ind][0], front_col[ind][1])
	t.down()
	t.setheading(start_angle - 7*10*(i+1)/5)
	t.forward(step)
	ind += 1

# Greenboard
t.up()
t.goto(-200, -350)
t.down()
t.setheading(0)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.up()
t.goto(-100, -425)
t.pencolor("dark green")
t.write("Greenboard", font=("Arial", 25))
t.hideturtle()
turtle.exitonclick()