from Tkinter import *
from Canvas import *

from scene import *
from scene.material import *
from geometry import *

import math


FIELD_OF_VIEW = math.pi / 4.0 #45 Grad
SCALE = 3
WIDTH = 400 * SCALE
HEIGHT = 300 * SCALE

redMat = Material(Color(255, 0, 0))
greenMat = Material(Color(0, 255, 0))
blueMat = Material(Color(0, 0, 255))

lightList = [Light(Point(30,30,10))]
objectList = [Sphere(Point(2.5,3,-10), 2, redMat),
              Sphere(Point(-2.5,3,-10), 2, greenMat),
              Sphere(Point(0,7,-10), 2, blueMat),
              Plane(Point(0,0,0), Vector(0,1,0))]

def render_pix(x, y, color):
    canvas.create_line(x,HEIGHT-y,x+1,HEIGHT-(y+1),fill=color.toHexString())


mw = Tk()
mw._root().wm_title("Raytracing")

# create and position canvas and buttons
cFrame = Frame(mw, width=WIDTH, height=HEIGHT)
cFrame.pack()
canvas = Canvas(cFrame, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

camera = Camera(Point(0,2,10), Vector(0,1,0), Point(0,3,0), FIELD_OF_VIEW)
camera.setScreenSize(WIDTH, HEIGHT)
camera.render(render_pix, objectList, lightList)

# start
mw.mainloop()
