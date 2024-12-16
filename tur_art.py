#Kaden Semanko
#11/26/24
#tur_art.py

import random as r #import random
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
move_random("purple") #changes color
move_random("aquamarine") #change color

<<<<<<< HEAD
def cool_thing(color): #bat logo
=======
def cool_thing(color): #it's a batman logo that you can alter the color
>>>>>>> e61ba90a15913b4d3854faf7ab44fce518e39deb
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
    red.right(135)
    red.forward(10)
    red.left(90)
    red.forward(10)
    red.right(135)
    red.forward(15)
    red.left(90)
    red.forward(10)
    red.left(90)
    red.forward(15)
    red.hideturtle() #allows the image to be looked without blocking

<<<<<<< HEAD
cool_thing("red")
cool_thing("blue")
turtle.done()
=======
cool_thing("red")#change pen color red
cool_thing("blue")#change pen color blue
turtle.done()#allow the image to be seen without closing
>>>>>>> e61ba90a15913b4d3854faf7ab44fce518e39deb
