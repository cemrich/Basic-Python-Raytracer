# -*- coding: utf-8 -*-

import math

class Vector(object):
    '''Basis-Vektorfunktionen im 3D-Raum'''
    
    def __init__(self, vec, y=0, z=0):
        '''Vector(1,2,3) oder Vector((1,2,3))'''
        if (type(vec) == tuple):
            self.vec = vec
        else:
            self.vec = (vec, y, z)
        self.vec = (float(self.vec[0]), float(self.vec[1]), float(self.vec[2]))
        
    def __repr__(self):
        return 'Vector(%s, %s, %s)' % (repr(self.x), repr(self.y), repr(self.z))

    def __add__(self, otherVec):
        '''Vector + Vector'''
        #assert(type(otherVec) == type(self))
        newVec = (self.vec[0]+otherVec.vec[0], \
                  self.vec[1]+otherVec.vec[1], \
                  self.vec[2]+otherVec.vec[2])
        return type(self)(newVec)
        
    def __sub__(self, otherVec):
        '''Vector - Vector'''
        #assert(type(otherVec) == type(self))
        newVec = (self.vec[0]-otherVec.vec[0], \
                  self.vec[1]-otherVec.vec[1], \
                  self.vec[2]-otherVec.vec[2])
        return type(self)(newVec)
    
    def __div__(self, num):
        '''Vector / Scalar'''
        #assert(type(num) == int or type(num) == float)
        newVec = (self.vec[0] / num, \
                  self.vec[1] / num, \
                  self.vec[2] / num)
        return type(self)(newVec)
    
    def __neg__(self):
        '-Vector = vector * -1'
        newVec = (-self.vec[0], \
                  -self.vec[1], \
                  -self.vec[2])
        return type(self)(newVec)

    def __mul__(self, num):
        '''Vector * Scalar oder Vector * Vector komponentenweise'''
        
        if type(num) == type(self):
            # Vector * Vector komponentenweise
            newVec = (self.vec[0] * num.vec[0], \
                      self.vec[1] * num.vec[1], \
                      self.vec[2] * num.vec[2])
        else:
            # Vector * Scalar
            newVec = (self.vec[0] * num, \
                      self.vec[1] * num, \
                      self.vec[2] * num)
            
        return type(self)(newVec)

    def __eq__(self, otherVec):
        return self.vec == otherVec.vec

    def length(self):
        '''Länge des Vektors'''
        return math.sqrt(self.vec[0]**2 + self.vec[1]**2 + self.vec[2]**2)

    def dot(self, otherVec):
        '''Skalarprodukt
        <Vector,Vector> = Scalar'''
        #assert(type(otherVec) == Vector)
        
        return self.vec[0]*otherVec.vec[0] + \
            self.vec[1]*otherVec.vec[1] + \
            self.vec[2]*otherVec.vec[2]

    def cross(self, otherVec):
        '''Vektorprodukt
        Vector X Vector = Vector'''
        #assert(type(otherVec) == type(self))
        
        x = self.vec[1]*otherVec.vec[2] - self.vec[2]*otherVec.vec[1]
        y = self.vec[2]*otherVec.vec[0] - self.vec[0]*otherVec.vec[2]
        z = self.vec[0]*otherVec.vec[1] - self.vec[1]*otherVec.vec[0]
        return type(self)(x, y, z)

    def scale(self, factor):
        '''Skaliert den Vektor
        Vector * Scalar = Vector'''
        return self * factor
        
    def normalized(self):
        '''Normalisiert den Vektor, sodass die Länge 1 ist'''
        return self / self.length()

    def inversed(self):
        '''invertierter Vektor
        Vector^-1 = Vector'''
        return type(self)(1/self.vec[0], 1/self.vec[1], 1/self.vec[2])

    def angle(self, otherVec):
        '''Winkel zwischen zwei Vektoren'''
        return math.acos(self.dot(otherVec) / (self.length() * otherVec.length()))

    def reflect(self, mirror):
        '''Reflektiert diesen Vektor an 'mirror'-Vektor'''
        # Ebene von self und mirror aufgespannt
        planeNormal = self.cross(mirror)
        # Spiegelebene
        mirrorNormal = planeNormal.cross(mirror).normalized()
        # Distanz zwischen self und Spiegelebene
        dist = self.cross(mirror.normalized()).length()
        # 2 mal die Distanz * Spiegelebene-Normale draufaddieren
        newPoint = self + mirrorNormal * dist * 2
        return type(self)(newPoint.vec)

    @property
    def x(self):
        return self.vec[0]
    
    @property
    def y(self):
        return self.vec[1]
    
    @property
    def z(self):
        return self.vec[2]

if __name__ == '__main__':

    print "Führe Tests aus..."

    vz = Vector(0,0,0)
    v = Vector(1.,2.,3.)
    v2 = Vector(2.,2.,2.)
    v3 = Vector(4.,3.,0)
    v4 = Vector(1.,1.,1.)
    v5 = Vector(1.,2.,1.)
    v6 = Vector(2.,-1.,3.)
    
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

    # Inverse testen
    assert(v.inversed() == Vector(1, 0.5, 1/3.0))

    # Winkel testen
    assert(Vector(5,0,0).angle(Vector(0,3,0)) == math.pi/2)
    assert(Vector(5,0,0).angle(Vector(3,3,0)) == math.pi/4)
    
    # Reflexion testen
    assert(Vector(1,1,0).reflect(Vector(1,0,0)) == Vector(1,-1,0))
    reflected = v2.reflect(v)
    assert(math.fabs(v2.angle(v) - reflected.angle(v)) < 0.000000001)

    print "Alle Tests erfolgreich"
