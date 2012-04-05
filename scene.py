from Tkinter import Tk, Frame, Canvas

from scene.light import Light
from scene.material import Material, Color
from scene.camera import Camera
from scene.sphere import Sphere
from scene.plane import Plane
from geometry import Point, Vector

import math

# Konstanten definieren
FIELD_OF_VIEW = math.pi / 4.0 #45 Grad
SCALE = 1
WIDTH = int(400 * SCALE)
HEIGHT = int(300 * SCALE)

# Materialien
planeMat = Material(Color(128, 128, 128), 1, 0.5, 0.5, 0.2)
redMat = Material(Color(255, 0, 0), 0.3, 0.8, 0.1)
greenMat = Material(Color(0, 255, 0), 0.3, 0.8, 0.2, 0.1)
blueMat = Material(Color(0, 0, 255), 0.3, 0.8, 0.2, 0.1)

# Szenen-Objekte
lightList = [Light(Point(30,30,10), 1), Light(Point(-1,20,-11), 0.2)]
objectList = [Sphere(Point(2.5,3,-10), 2, redMat),
              Sphere(Point(-2.5,3,-10), 2, greenMat),
              Sphere(Point(0,7,-10), 2, blueMat),
              Plane(Point(0,0,0), Vector(0,1,0), planeMat)]

# Renderfunktion - wird pro Pixel aufgerufen
def render_pix(x, y, color):
    canvas.create_line(x,HEIGHT-y,x+1,HEIGHT-(y+1),fill=color.toHexString())


mw = Tk()
mw._root().wm_title("Raytracing")

# create and position canvas and buttons
cFrame = Frame(mw, width=WIDTH, height=HEIGHT)
cFrame.pack()
canvas = Canvas(cFrame, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# camera initialisieren
camera = Camera(Point(0,2,10), Vector(0,1,0), Point(0,3,0), FIELD_OF_VIEW)
camera.setScreenSize(WIDTH, HEIGHT)
camera.render(render_pix, objectList, lightList)

# start
mw.mainloop()
