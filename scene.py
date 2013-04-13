# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Canvas, PhotoImage

from scene.light import Light
from scene.material import Material, CheckedMaterial, Color
from scene.camera import Camera
from scene.sphere import Sphere
from scene.plane import Plane
from scene.triangle import Triangle
from geometry import Point, Vector

import math

# Konstanten definieren
FIELD_OF_VIEW = math.pi / 4.0 #45 Grad
SCALE = 1 #zum Schnellen Vergrößern/Verkleinern
WIDTH = int(320 * SCALE)
HEIGHT = int(240 * SCALE)

# Materialien
planeMat = CheckedMaterial()
redMat = Material(Color(1, 0, 0), 0.3, 0.8, 0.1)
greenMat = Material(Color(0, 1, 0), 0.3, 0.8, 0.2, 0.1)
blueMat = Material(Color(0, 0, 1), 0.3, 0.8, 0.2, 0.1)
triangleMat = Material(Color(1, 1, 0), 0.3, 0.8, 0.1, 0)

# Szenen-Objekte
lightList = [Light(Point(30,30,10), 1)]
objectList = [Sphere(Point(2.5,3,-10), 2, redMat),
              Sphere(Point(-2.5,3,-10), 2, greenMat),
              Sphere(Point(0,7,-10), 2, blueMat),
              Triangle(Point(2.5,3,-10), Point(-2.5,3,-10), Point(0,7,-10), triangleMat),
              Plane(Point(0,0,0), Vector(0,1,0), planeMat)]

# Renderfunktion - wird pro Pixel aufgerufen
def render_pix(x, y, color):
    img.put(color.toValidatedHexString(), (x, HEIGHT-y))


mw = Tk()
mw._root().wm_title("Raytracing")

# create and position canvas
cFrame = Frame(mw, width=WIDTH, height=HEIGHT)
cFrame.pack()
canvas = Canvas(cFrame, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)

# camera initialisieren
camera = Camera(Point(0,2,10), Vector(0,1,0), Point(0,3,0), FIELD_OF_VIEW)
camera.setScreenSize(WIDTH, HEIGHT)
camera.render(render_pix, objectList, lightList)

# draw finished image
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

# start
mw.mainloop()
