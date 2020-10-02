import turtle 
window=turtle.Screen() 
window.bgcolor("black")


turtle=turtle.Turtle() 
turtle.shape("turtle")
turtle.color("red")
turtle.width(50)
turtle.speed(5)
colors=["red","white","cyan","pink","lightblue","hotpink","orange","coral","silver","green"]
def heart():
    for blood in range(43):
        turtle.pencolor(colors[blood%9])
        turtle.right(5)
        turtle.forward(5)
    turtle.forward(150)
    turtle.penup()
    turtle.right(140)
    turtle.forward(147)
    turtle.pendown()
    for blood in range(43):
        turtle.pencolor(colors[blood%9])
        turtle.left(5)
        turtle.forward(5)
    turtle.left(7)
    turtle.forward(151)
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
heart()


window.exitonclick() 
