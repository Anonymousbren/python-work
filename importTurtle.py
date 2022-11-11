from asyncio import run
import turtle
t = turtle.Turtle()

#for background
screen = turtle.Screen
screen.bgcolor('black')
#creating a rectangle
t.color('white')
t.shape('arrow')
t.speed()
t.fillcolor('blue')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(200)
t.forward(200)
t.left(90)
t.forward(200)
t.end_fill()
turtle.done()

if __name__ == '__main__':
         run()







