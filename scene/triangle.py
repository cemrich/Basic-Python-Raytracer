# -*- coding: utf-8 -*-

from material import Material

class Triangle(object):
    '''
    Einfaches Dreieck im Raum.
    '''

    def __init__(self, p1, p2, p3, material=None):
        '''
        @param p1: erster Eckpunkt
        @param p2: zweiter Eckpunkt
        @param p3: dritter Eckpunkt
        @param material: Material, default: Material()
        '''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.u = p2 - p1
        self.v = p3 - p1
        self.normal = self.u.cross(self.v).normalized()

        self.material = material if material else Material()

        print "Dreieck initialisiert:", repr(self)

    def __repr__(self):
        return "Triangle(%s, %s, %s)" % (repr(self.p1), repr(self.p2), repr(self.p3))

    def intersectionParameter(self, ray):
        '''
        Schneidet den übergebenen Strahl mit dem Objekt und
        gibt den errechneten Abstand zurück.
        @param ray:  Strahl, mit dem geschnitten werden soll
        @return:     Abstand des Strahlenursprungs von dem Objekt oder None
        '''
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
            
        w = ray.origin - self.p1
        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        if r < 0 or r > 1:
            return None
          
        s = wu.dot(ray.direction) / dvu
        if s >= 0 and s <= 1 and r + s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        '''
        @param point: Punkt an dem die Normale des Objektes gesucht is
        @return:      Normale des Objektes am gegebenen Punkt
        '''
        return self.normal
