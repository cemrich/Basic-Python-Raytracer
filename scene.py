# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame, Canvas, PhotoImage, NW

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
RENDER_LEVEL = 3

# Materialien
planeMat = CheckedMaterial(0.2)
redMat = Material(Color(1, 0, 0))
greenMat = Material(Color(0, 1, 0))
blueMat = Material(Color(0, 0, 1))
triangleMat = Material(Color(1, 1, 0))

# Szenen-Objekte
lightList = [Light(Point(30,30,10), Color(1, 1, 1))]
objectList = [Sphere(Point(2.5,3,-10), 2, redMat),
              Sphere(Point(-2.5,3,-10), 2, greenMat),
              Sphere(Point(0,7,-10), 2, blueMat),
              Triangle(Point(2.5,3,-10), Point(-2.5,3,-10), Point(0,7,-10), triangleMat),
              Plane(Point(0,0,0), Vector(0,1,0), planeMat)]

# Renderfunktion - wird pro Pixel aufgerufen
def render_pix(x, y, color):
    img.put(color.toValidatedHexString(), (x, HEIGHT-y))
    if x%320 == 0:
        canvas.update()

# Fenster & Canvas aufbauen
mw = Tk()
mw._root().wm_title("Raytracer")

cFrame = Frame(mw, width=WIDTH, height=HEIGHT)
cFrame.pack()
canvas = Canvas(cFrame, width=WIDTH, height=HEIGHT, bg="white")

# Bild für Pixelunterstützung
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image(0, 0, image=img, anchor=NW)
canvas.pack()

# camera initialisieren
camera = Camera(Point(0,2,10), Vector(0,1,0), Point(0,3,0), FIELD_OF_VIEW)
camera.setScreenSize(WIDTH, HEIGHT)

# Anfangen zu Rendern, nachdem Canvas sichtbar ist
mw.wait_visibility()
camera.render(render_pix, objectList, lightList, level=RENDER_LEVEL)

# start
mw.mainloop()
