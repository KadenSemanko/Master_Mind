#Kaden Semanko
#11/26/24
#graphics.py
import turtle as tur
tur.speed(100)
tur.shapesize(2)
tur.shape("turtle")

tur.color("green") # wanted color
for i in range(3): #repeat 3 times for the final side to be created without extra
    tur.forward(100)
    tur.left(90)

tur.forward(100) #final line

tur.color("white") #allowing for space
tur.forward(100)

tur.color("orange") # colored hexagon 6 sides that are equalateral and equalangular
for i in range(6):
    tur.forward(100)
    tur.right(60)

tur.left(90) #adjusting to not make it a open shape
tur.color("white")
tur.forward(100) #making space

tur.color("red")# the color
tur.forward(50) 
tur.right(60)
for i in range(2): # allows for the same sides to repeat
    tur.forward(25)
    tur.right(60)
tur.forward(50)
for i in range(2):
    tur.right(60)
    tur.forward(25)

tur.left(75)
tur.color("white") #adding more space so sides don't overlap
tur.forward(200)

tur.color("blue") 
tur.left(30) #it will go off 
for i in range(2): #two sides of congruent sides to make a rectangle
    tur.forward(200)
    tur.right(90)
    tur.forward(12)
    tur.right(90)

tur.left(80)
tur.color("white")
tur.forward(50)

def hectogon(): #Function for the "circle" to make it easier to repeat
    for i in range(100):
        tur.color("black") 
        tur.forward(1)
        tur.left(3.6)
hectogon() # 1 of 3 circles

tur.right(60) #spacing
tur.color("white")
tur.forward(20)

hectogon() # 2nd of 3 circles

tur.right(60)
tur.color("white") #extra space so I don't run into the rest of the shapes
tur.forward(20)
tur.left(60)
tur.forward(20)

hectogon() # final circle

tur.done() #allows the final image to be seen
