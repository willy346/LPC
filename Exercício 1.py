import turtle
import math

def plot_fibonacci(n):
    x = 0
    y = 1
    square_x = x
    square_y = y
    
    s.pencolor("red")
    
    s.forward(y * factor)
    s.left(90)
    s.forward(y * factor)
    s.left(90)
    s.forward(y * factor)
    s.left(90)
    s.forward(y * factor)
    
    temp = square_y
    square_y += square_x
    square_x = temp
    
    for i in range(1, n):
        s.backward(square_x * factor)
        s.right(90)
        s.forward(square_y * factor)
        s.left(90)
        s.forward(square_y * factor)
        s.left(90)
        s.forward(square_y * factor)
        
        temp = square_y
        square_y += square_x
        square_x = temp
        
    s.penup()
    s.setposition(factor, 0)
    s.seth(0)
    s.pendown()
    s.pencolor("Blue")
    s.left(90)
    
    for i in range(n):
        print(y)
        fdwd = math.pi*y*factor/2
        fdwd /= 90
        
        for j in range(90):
            s.forward(fdwd)
            s.left(1)
        temp = x
        x = y
        y += temp
 
       
factor = 1
 
n = int(input("Enter the number of iterations: "))

if n > 0:
    print("Fibonacci series for", n, "elements:")
    s = turtle.Turtle()
    s.speed(100)
    plot_fibonacci(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")   
    