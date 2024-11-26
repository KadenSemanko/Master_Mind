#Kaden Semanko
#11/26/24
#tur_art.py

import random as r
import turtle #import turtle
turtle.hideturtle()
blue = turtle.Turtle() #created one of two turtles
red = turtle.Turtle() # 2nd turtle
def move_random(color): # you can alter color of shape
    blue.speed(10000) #it's slow
    blue.penup() # so it doesn't run off screen as much
    blue.backward(250)
    blue.pendown()
    blue.color(color)
    for i in range(50):
        a = r.randint(1,200) # random use case
        blue.forward(a)
        blue.left(90) # all degrees are 90
        if a == 90:
            for l in range(100):
                blue.color("black")  #makes a hectogon if a == 90 colored  black
                blue.forward(1)
                blue.left(3.6)
#move_random("purple")
#move_random("aquamarine")

def cool_thing(color):
    red.color(color)
    red.forward(100)
    red.right(135)
    red.forward(50)
    red.right(45)
    red.forward(70)
    red.left(60)
    red.forward(25)
    red.right(120)
    red.forward(25)
    red.left(60)
    red.forward(70)
    red.right(45)
    red.forward(50)
    red.right(135)
    red.forward(100)
    red.right(90)
    red.forward(15)
    red.left(90)
    red.forward(10)
    red.left(90)
    red.forward(15)
    red.right(180)
    red.forward(8)
    red.forward(10)
    red.left(90)
    red.forward(8)

cool_thing("red")
#cool_thing("blue")
turtle.done()