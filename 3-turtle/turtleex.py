import turtle

window = turtle.Screen()

nick = turtle.Turtle()

nick.speed(10)

nick.left(90)
nick.forward(100)
nick.right(135)
nick.forward(142)
nick.left(135)
nick.forward(100)
nick.right(90)
nick.penup()
nick.forward(50)
nick.pendown()
nick.right(90)
nick.forward(100)
nick.right(180)
nick.forward(100)
nick.right(90)
nick.forward(20)
for i in range(180):
    nick.forward(0.5)
    nick.right(1)
nick.forward(20)
nick.left(135)
nick.forward(71)

window.exitonclick()
