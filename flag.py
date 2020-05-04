from turtle import Turtle, Screen, done

width = 400
height = width * 6 / 10
initial_position = (-200, 300)


screen = Screen()
screen_width = 700
screen_height = 750
bkg_width = screen_width - 30
bkg_height = screen_height - 30
screen.setup(screen_width, screen_height)
turtle = Turtle()

# draw ground
turtle.pu()
turtle.color("#003300", "#003300")
turtle.setposition(-bkg_width/2, -bkg_height/2 + 150)

turtle.begin_fill()
turtle.pd()
for _ in range(2):
    turtle.forward(bkg_width)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
turtle.end_fill()

# draw sky
turtle.color("#34c3eb")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(bkg_width)
    turtle.left(90)
    turtle.forward(bkg_height - 150)
    turtle.left(90)
turtle.end_fill()

# go to stick drawing position\
turtle.color("black", "black")
turtle.penup()
turtle.setposition(*initial_position)
turtle.left(90)

# draw stick
turtle.begin_fill()
turtle.pd()
for _ in range(2):
    turtle.left(90)
    turtle.forward(height/30)
    turtle.left(90)
    turtle.forward(width + height - 50)
turtle.end_fill()
turtle.pu()

# Move to rect drawing position
turtle.right(180)
turtle.forward(height/50)
turtle.left(90)
turtle.forward(1)

# Draw green rect
turtle.color("#006747", "#006747")
turtle.pendown()

# draw rect
turtle.begin_fill()
for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.color("#DA291C", "#DA291C")

# go to circle drawing position
turtle.forward(width * 45 / 100)
turtle.right(90)
turtle.forward(height / 6)
turtle.right(90)

# draw circle
turtle.pendown()
turtle.begin_fill()
turtle.circle(width * 2 / 10)
turtle.end_fill()

# go to right edge
turtle.color("black", "black")
turtle.pu()
turtle.forward(width * 45 / 100)
turtle.right(90)
turtle.forward(height / 6 + height/50)

turtle.hideturtle()


done()


