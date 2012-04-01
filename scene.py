from Tkinter import *
from Canvas import *

from scene import *
from geometry import *

import math


FIELD_OF_VIEW = math.pi / 4.0 # 45 Grad
WIDTH = 200
HEIGHT = 150

lightList = [Light(Point(30,30,10))]
objectList = [Sphere(Point(2.5,3,-10), 2),
              Sphere(Point(-2.5,3,-10), 2),
              Plane(Point(0,0,0), Vector(0,1,0)),
              Sphere(Point(0,7,-10), 2)]

def render_pix(x, y, r, g, b):
    hexcolor = '#%02X%02X%02X'%(r,g,b)
    canvas.create_line(x,HEIGHT-y,x+1,HEIGHT-(y+1),fill=hexcolor)


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
