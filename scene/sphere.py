# -*- coding: utf-8 -*-

import math
from material import Material

class Sphere(object):
    '''
    Eine einfache Kugel im Raum.
    '''
    
    def __init__(self, center, radius, material=None):
        '''
        @param center:   Mittelpunkt der Kugel
        @param radius:   Radius der Kugel
        @param material: Material, default: Material()
        '''
        self.center = center # point
        self.radius = radius # vector
        self.radiusSquared = radius ** 2 # caching for performance

        self.material = material if material else Material()

        print "Kugel initialisiert:", repr(self)

    def __repr__(self):
        return 'Sphere(%s,%s)' % (repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        '''
        Schneidet den übergebenen Strahl mit dem Objekt und
        gibt den errechneten Abstand zurück.
        @param ray:  Strahl, mit dem geschnitten werden soll
        @return:     Abstand des Strahlenursprungs von dem Objekt oder None
        '''
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v**2 - co.dot(co) + self.radiusSquared
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        '''
        @param point: Punkt an dem die Normale des Objektes gesucht is
        @return:      Normale des Objektes am gegebenen Punkt
        '''
        return (p - self.center).normalized()



        
        
