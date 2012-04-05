# -*- coding: utf-8 -*-

from geometry import Vector
import math


class Material(object):

    def __init__(self, color=None, ambient=0, diffuse=0.8, specular=0.2, glossiness=0.05):
        '''
        color als Color
        ambient: Anteil an ambientem Lichts (0-1)
        diffuse: Anteil an diffusem Lichts (0-1)
        specular: Anteil an spekularem Lichts (0-1)
        glossiness: konstanter Faktor zur Beschreibung der Oberflächenbeschaffenheit 
                    (0 => rau, 1 => perfekter Spiegel)
           
        ambient + diffuse <= 1
        '''
        self.color = color
        if not color:
            self.color = Color(128, 128, 128)
        
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.n = 64 * glossiness + 1
        self.glossiness = glossiness
        
    def renderColor(self, lightRay, normal, lightIntensity, rayDirection):
        '''
        Gibt die Farbe dieses Materials für eine bestimmte Lichtqualität zurück.
        @param lightRay: Strahl vom zu rendernden Punkt zur Lichtquelle (Ray)
        @param normal: Normale an der zu rendernden Stelle (Vector)
        @param lightIntensity: Intensität der Lichtquelle (0-1)
        @param rayDirection: Blickrichtung auf die zu rendernde Stelle (Vector)
        @return: Farbe dieses Materials (Color)
        '''
        color = black
        reflectedLight = (lightRay.direction).reflect(normal)
        diffuseFactor = lightRay.direction.dot(normal)
    
        if (diffuseFactor > 0):
            color += self.color * (diffuseFactor*self.diffuse) * lightIntensity
            specularFactor = reflectedLight.dot(rayDirection * -1)
            if specularFactor > 0:
                specConst = (self.n + 2) / (math.pi *2)
                color += white * specConst * (specularFactor**self.n * self.specular) * lightIntensity
        return color


class Color(Vector):
    
    def __init__(self, r, g=0, b=0):
        Vector.__init__(self, r, g, b)

    def validate(self):
        return Color(tuple([255 if c > 255 else c for c in self.vec]))

    def __mul__(self, other):
        return super(Color, self).__mul__(other)

    def __add__(self, other):
        return super(Color, self).__add__(other)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def toHexString(self):
        return '#%02X%02X%02X' % (self.r, self.g, self.b)

black = Color(0, 0, 0)
white = Color(255, 255, 255)