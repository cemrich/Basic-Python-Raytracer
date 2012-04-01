# -*- coding: utf-8 -*-

import math
from ray import Ray

class Camera(object):
    def __init__(self, position, up, f_point, fieldOfView):
	'''
	position:    wo steht die Camera (Point)
	up:          welche Richtung ist Oben (Vector)
	f_point:     auf welchen Punkt schaut die Camera (Point)
	fieldOfView: Öffnungswinkel im Bogenmaß
	'''
        self.position = position
        self.up = up
        self.f_point = f_point
        self.fieldOfView = fieldOfView

        self.z = (f_point-position).normalized()
        self.x = self.z.cross(up).normalized()
        self.y = self.x.cross(self.z)

        print "Camera initialisiert:", repr(self)

    def setScreenSize(self, width, height):
        self.width = width
        self.height = height
        ratio = width / float(height)
        alpha = self.fieldOfView / 2.0
        print "alpha:", alpha
        self.sceneHeight = 2 * math.tan(alpha)
        print "sceneHeight:", self.sceneHeight
        self.sceneWidth = ratio * self.sceneHeight
        print "sceneWidth:", self.sceneWidth
        self.pixelWidth = self.sceneWidth / (width-1)
        print "pixelWidth:", self.pixelWidth
        self.pixelHeight = self.sceneHeight / (height-1)
        print "pixelHeight:", self.pixelHeight

    def build_ray(self, x, y):
        xComp = self.x * (x*self.pixelWidth - self.sceneWidth/2.0)
        yComp = self.y * (y*self.pixelHeight - self.sceneHeight/2.0)
        return Ray(self.position, self.z + xComp + yComp)

    def colorFromDistance(self, distance):
        colorMaxDist = 21
        colorMinDist = 18
        if distance < colorMaxDist:
            if distance <= colorMinDist: # zu nah dran -> dunkel
                colorValue = 0
            else: # mitte -> grau
                colorValue = (distance-colorMinDist)/(colorMaxDist-colorMinDist)*255
        else: #weit weg -> hell
            colorValue = 255

        return colorValue

    def getMinDist(self, ray, objectList):
        minDist = float('inf')
        for obj in objectList:
            hitDist = obj.intersectionParameter(ray)
            if hitDist and hitDist > 0 and hitDist < minDist:
                minDist = hitDist
        return minDist

    def render(self, render_func, objectList):
        steps = 1
        for y in range(0, self.height, steps):
            for x in range(0, self.width, steps):
                ray = self.build_ray(x, y)
                minDist = self.getMinDist(ray, objectList)
                colorValue = self.colorFromDistance(minDist)
                render_func(x, y, colorValue, colorValue, colorValue) 
		
    def __repr__(self):
        return 'Camera(position:%s, up:%s, f_point:%s, fieldOfView:%s, x:%s, y:%s, z:%s)' % (repr(self.position), repr(self.up), repr(self.f_point), repr(self.fieldOfView), repr(self.x), repr(self.y), repr(self.z))
