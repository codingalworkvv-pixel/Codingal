import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(300,400)


polygon = turtle.Turtle()
for i in range(20):
    polygon.forward(i*5)
    polygon.right(90)



turtle.done()
    
