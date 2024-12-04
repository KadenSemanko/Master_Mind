import turtle as tur
def x2_minus3x_plus4(x):
    return x**2 - 3*x + 4

print(x2_minus3x_plus4(5))
def genquad(a,b,c,x): # 4 values that are defined 
    return (a* (x ** 2)) +(b * x) + c
print(genquad(1,2,3,4)) 

def test(x): #you input x value
    tur.pencolor("white") # I'm making a point so I want to jump to the point without marks
    x2_minus3x_plus4(x)
    if x < 0:
        x = x*-1 # allows for correct movement technically not necessary
        value = tur.backward(x) #left movement
    elif x > 0:
        value = tur.forward(x) #right movement
    tur.left(90)
    y = x2_minus3x_plus4(x)
    if y < 0: 
        y = y*-1 # technically not appicable but if I did a different function
        num = tur.backward(y) 
    elif y > 0:
        num = tur.forward(y) # sets the y value for the related x
    value 
    num
test(17)
tur.screensize(10000000,10000000)
math_t = tur.Turtle()
math_t.teleport(0,x2_minus3x_plus4(0))
for i in range(1,400):
    math_t.goto(i,x2_minus3x_plus4(i))
tur.done()
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab
import numpy 

ax = a3.Axes3D(pylab.figure())
for i in range(10000):
    vtx = numpy.random.rand(3,3)
    tri = a3.art3d.Poly3DCollection([vtx])
    tri.set_color(colors.rgb2hex(numpy.random.rand(3)))
    tri.set_edgecolor('k')
    ax.add_collection3d(tri)
pylab.show()