import turtle

turtle.pensize(4)
turtle.color('red', 'blue')

turtle.penup()
turtle.goto(-130, 50)
turtle.pendown()

turtle.begin_fill()
for i in range(5):
    turtle.fd(100)
    turtle.lt(72)
    turtle.fd(100)
    turtle.rt(144)
turtle.end_fill()

turtle.mainloop()