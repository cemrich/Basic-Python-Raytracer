# -*- coding: utf-8 -*-

import math
from ray import Ray
import material

class Camera(object):
    def __init__(self, position, up, f_point, fieldOfView):
        '''
        @param position:    wo steht die Camera (Point)
        @param up:          welche Richtung ist Oben (Vector)
        @param f_point:     auf welchen Punkt schaut die Camera (Point)
        @param fieldOfView: Öffnungswinkel im Bogenmaß
        '''
        self.inf = float('inf')
      
        self.position = position
        self.up = up
        self.f_point = f_point
        self.fieldOfView = fieldOfView

        self.z = (f_point-position).normalized()
        self.x = self.z.cross(up).normalized()
        self.y = self.x.cross(self.z)

        print "Camera initialisiert:", repr(self)

    def setScreenSize(self, width, height):
        '''
        Initiiert den Viewport
        @param width: Breite des gerenderten Bildes in Pixeln
        @param height: Höhe des gerenderten Bildes in Pixeln
        '''
        self.width = width
        self.height = height
        ratio = width / float(height)
        alpha = self.fieldOfView / 2.0
        print "alpha:", alpha
        self.halfSceneHeight = math.tan(alpha)
        print "halfSceneHeight:", self.halfSceneHeight
        self.halfSceneWidth = ratio * self.halfSceneHeight
        print "halfSceneWidth:", self.halfSceneWidth
        self.pixelWidth = self.halfSceneWidth / (width-1) * 2
        print "pixelWidth:", self.pixelWidth
        self.pixelHeight = self.halfSceneHeight / (height-1) * 2
        print "pixelHeight:", self.pixelHeight
        self.pixelWidthVec = self.x * self.pixelWidth    #caching for better performance in build_ray
        self.pixelHeightVec = self.y * self.pixelHeight  #caching for better performance in build_raypixelWidth    #caching for better performance in build_ray
        self.halfSceneWidthVec = self.x * self.halfSceneWidth    #caching for better performance in build_ray
        self.halfSceneHeightVec = self.y * self.halfSceneHeight  #caching for better performance in build_ray

    def build_ray(self, x, y):
        '''
        Gibt einen Strahl zurück, der von der Kamera durch die 
        angegebene x/y-Pixel-Koordinate geht.
        '''
        xComp = self.pixelWidthVec * x - self.halfSceneWidthVec
        yComp = self.pixelHeightVec * y - self.halfSceneHeightVec
        return Ray(self.position, self.z + xComp + yComp)

    def getMinDistAndObj(self, ray, objectList):
        '''
        Gibt das am nächsten gelegene Objekt zurück.
        @param ray: Blickrichtung der Kamera durch den aktuellen Pixel
        @param objectList: Liste aller Objekte in der Szene
        @return: Tupel aus Distanz und nächstem Objekt
        '''
        minDist = self.inf
        minObject = None
        for obj in objectList:
            dist = obj.intersectionParameter(ray)
            if dist and dist > 0 and dist < minDist:
                minDist = dist
                minObject = obj
        return (minDist, minObject)

    def isInShadow(self, objectList, lightRay):
        '''
        Berechnet, ob der Strahl von Objekten geschnitten wird.
        @param objectList: Liste aller Objekte in der Szene
        @param lightRay: Strahl von einem Objekt zu einer Lichtquelle
        @return: 0 wenn die Lichtquelle vom Objekt aus sichtbar ist, > 0 sonst
        '''
        for obj in objectList:
            t = obj.intersectionParameter(lightRay)
            return t if t > 0 else 0

    def calculateColor(self, objectList, lightList, rayDir, point, obj):
        '''
        Gibt die Objektfarbe an der entsprechenden Stelle zurück (ohne Reflexionen).
        @param objectList: Liste aller Objekte in der Szene
        @param lisghtList: Liste aller Lichter in der Szene
        @param rayDir: Richtung des Sichtstrahls auf die Stelle (Vector)
        @param point: Punkt in der Szene, der berechnet werden soll
        @param object: Objekt an der zu berechnenden Stelle
        @return: Objektfarbe ohne Reflexionen (Color)
        '''
        normal = obj.normalAt(point)
        color = obj.material.ambientColor
        
        for light in lightList:
            lightRay = Ray(point, light.position-point)
            if not self.isInShadow(objectList, lightRay):
                color += obj.material.renderColor(lightRay, normal, light.intensity, rayDir)
        
        return color
    
    def renderRay(self, objectList, lightList, ray, bgColor, level):
        '''
        Rendert genau einen  Sichtstrahl der Kamera.
        @param objectList: Liste aller Objekte in der Szene
        @param lisghtList: Liste aller Lichter in der Szene
        @param ray: Strahl, der in die Richtung zeigt, die gerendert werden soll
        @param bgColor: Hintergrundfarbe (Color)
        @param level: aktuelles Renderlevel
        @return: Farbe an dieser Stelle (Color)
        '''
        (dist, obj) = self.getMinDistAndObj(ray, objectList)
        
        if dist > 0 and dist < self.inf:
            point = ray.origin + ray.direction * dist
            color = self.calculateColor(objectList, lightList, ray.direction, point, obj)
            
            if level == 0:
                return color
              
            normal = obj.normalAt(point)
            reflectedRay = Ray(point, ray.direction.reflect(normal)*-1)
            reflectedColor = self.renderRay(objectList, lightList, reflectedRay, bgColor, level-1)
            return color*(1-obj.material.glossiness) + reflectedColor * obj.material.glossiness
        else:
            return bgColor
       
    def render(self, render_func, objectList, lightList, bgColor=material.black, level=1):
        '''
        Rendert das aktuelle Kamerabild pixelweise.
        @param render_func: Funktion, die zum Tatsächlichen render aufgerufen wird: render_func(x, y, color)
        @param objectList: Liste aller Objekte in der Szene
        @param lisghtList: Liste aller Lichter in der Szene
        @param bgColor: Hintergrundfarbe (Color)
        @param level: Anzahl der Renderlevel (0 => keine Reflexionen, 1 => ein Level von Reflexionen)
        '''
        for y in range(self.height+1):
            for x in range(self.width+1):
                ray = self.build_ray(x, y)
                color = self.renderRay(objectList, lightList, ray, bgColor, level)
                render_func(x, y, color)
    
    def __repr__(self):
        return 'Camera(position:%s, up:%s, f_point:%s, fieldOfView:%s, x:%s, y:%s, z:%s)' % (repr(self.position), repr(self.up), repr(self.f_point), repr(self.fieldOfView), repr(self.x), repr(self.y), repr(self.z))
