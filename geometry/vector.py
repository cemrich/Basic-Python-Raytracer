# -*- coding: utf-8 -*-

import math

class Vector(object):
    def __init__(self, vec, y=0, z=0):
        if (type(vec) == tuple):
            self.vec = vec
        else:
            self.vec = (vec, y, z)
        (self.x, self.y, self.z) = self.vec
        self.vec = tuple(map(float, self.vec))

    def __repr__(self):
        return 'Vector(%s, %s, %s)' % (repr(self.x), repr(self.y), repr(self.z))

    def __add__(self, otherVec):
        '''Vector + Vector'''
        assert(type(otherVec) == Vector)
        newVec = tuple(map(lambda coords: coords[0]+coords[1], zip(self.vec, otherVec.vec)))
        return Vector(newVec)
        
    def __sub__(self, otherVec):
        '''Vector - Vector'''
        assert(type(otherVec) == Vector)
        newVec = tuple(map(lambda coords: coords[0]-coords[1], zip(self.vec, otherVec.vec)))
        return Vector(newVec)
    
    def __div__(self, num):
        '''Vector / Scalar'''
        assert(type(num) == int or type(num) == float)
        newVec = tuple(map(lambda coord: coord/num, self.vec))
        return Vector(newVec)

    def __mul__(self, num):
        '''Vector * Scalar'''
        assert(type(num) == int or type(num) == float)
        newVec = tuple(map(lambda coord: coord*num, self.vec))
        return Vector(newVec)

    def __eq__(self, otherVec):
        return self.vec == otherVec.vec

    def length(self):
        newVec = map(lambda coord: coord**2, self.vec)
        return math.sqrt(newVec[0] + newVec[1] + newVec[2])

    def dot(self, otherVec):
        '''Skalarprodukt
        <Vector,Vector> = Scalar'''
        assert(type(otherVec) == Vector)
        
        # Elemente multiplizieren
        newVec = tuple(map(lambda coords: coords[0]*coords[1], zip(self.vec, otherVec.vec)))
        return newVec[0] + newVec[1] + newVec[2]

    def cross(self, otherVec):
        '''Vektorprodukt
        Vector X Vector = Vector'''
        assert(type(otherVec) == Vector)
        
        x = self.y*otherVec.z - self.z*otherVec.y
        y = self.z*otherVec.x - self.x*otherVec.z
        z = self.x*otherVec.y - self.y*otherVec.x
        return Vector(x, y, z)

    def scale(self, factor):
        return self * factor
        
    def normalized(self):
        return self / self.length()


if __name__ == '__main__':

    print "Führe Tests aus..."

    vz = Vector(0,0,0)
    v = Vector(1,2,3)
    v2 = Vector(2,2,2)
    v3 = Vector(4,3,0)
    v4 = Vector(1,1,1)
    v5 = Vector(1,2,1)
    v6 = Vector(2,-1,3)
    
    # Addition testen
    assert(v+v2 == Vector(3, 4, 5))

    # Subtraktion testen
    assert(v-v2 == Vector(-1, 0, 1))

    # Skalarprodukt testen
    assert(v.dot(v2) == 12)
    assert(v.dot(v2) == v2.dot(v))

    # Länge testen
    assert(v3.length() == 5)

    # Division testen
    assert(v3 / 2 == Vector(2, 3/2.0, 0))

    # Normalisierung testen
    assert(v.normalized().length() == 1)

    # Skalierung testen
    assert(v.scale(5) == v*5)

    # Vektorprodukt testen
    assert(v2.cross(v4) == vz)
    assert(v4.cross(v2) == vz)
    assert(v5.cross(v6) == Vector(7,-1,-5))

    print "Alle Tests erfolgreich"
