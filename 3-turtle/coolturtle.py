import turtle

window = turtle.Screen()

nick = turtle.Turtle()

nick.speed(10)

for i in range(180):
    nick.forward(100)
    nick.right(30)
    nick.forward(20)
    nick.left(60)
    nick.forward(50)
    nick.right(30)

    nick.penup()
    nick.setposition(0, 0)
    nick.pendown()

    nick.right(2)

window.exitonclick()
