from turtle import *

speed('fastest')

rt(-90)


angle = 30

def fractal(size, level):
    
    if level > 0:
        colormode(255)
        
        pencolor(0, 255//level, 0)
        
        fd(size) 
        rt(angle)
        
        fractal(0.8 * size, level - 1)
        pencolor(0, 255//level, 0)
        
        lt(2 * angle)
        
        fractal(0.8 * size, level - 1)
        pencolor(0, 255//level, 0)
        
        rt(angle)
        fd(-size)

fractal(80, 7)