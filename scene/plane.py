# -*- coding: utf-8 -*-

from material import Material

class Plane(object):
    '''
    Einfache Fläche im Raum.
    '''

    def __init__(self, point, normal, material=None):
        '''
        @param point:     ein Punkt, der auf der Ebene liegt
        @param normal:    Normale der Ebene
        @param material:  Material, default: Material()
        '''
        self.point = point
        self.normal = normal.normalized()
        self.material = material if material else Material()
        
        print "Fläche initialisiert:", repr(self)

    def __repr__(self):
        return "Plane(%s, %s)" % (repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        '''
        Schneidet den übergebenen Strahl mit dem Objekt und
        gibt den errechneten Abstand zurück.
        @param ray:  Strahl, mit dem geschnitten werden soll
        @return:     Abstand des Strahlenursprungs von dem Objekt oder None
        '''
        op = ray.origin - self.point
        b = ray.direction.dot(self.normal)
        return -op.dot(self.normal) / b if b else None

    def normalAt(self, point):
        '''
        @param point: Punkt an dem die Normale des Objektes gesucht is
        @return:      Normale des Objektes am gegebenen Punkt
        '''
        return self.normal
