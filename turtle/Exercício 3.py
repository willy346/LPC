import turtle

scr = turtle.Screen()
tess = turtle.Turtle()

def triangle(a, b):
    tess.penup()
    tess.goto(a, b)
    tess.pendown()
    
    for i in range(3):
        tess.forward(100)
        tess.left(120)
        tess.forward(100)
        
turtle.onscreenclick(triangle, 1)
turtle.listen()

turtle.done()