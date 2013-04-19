# -*- coding: utf-8 -*-

from vector import Vector

class Point(object):
    '''Basis-Punktoptionen im 3D-Raum'''
    
    def __init__(self, point, y=0, z=0):
        '''Point(1,2,3) oder Point((1,2,3))'''
        if (type(point) == tuple):
            self.point = point
        else:
            self.point = (point, y, z)
        #self.point = (float(self.point[0]), float(self.point[1]), float(self.point[2]))

    def __repr__(self):
        return 'Point(%s, %s, %s)' % (repr(self.point[0]), repr(self.point[1]), repr(self.point[2]))

    def __eq__(self, otherPoint):
        return self.point == otherPoint.point

    def __sub__(self, otherPoint):
        '''Point - Point = Vector'''
        #assert(type(otherPoint) == Point)
        newVec = (self.point[0]-otherPoint.point[0], \
                  self.point[1]-otherPoint.point[1], \
                  self.point[2]-otherPoint.point[2])
        return Vector(newVec)

    def __add__(self, vector):
        '''Point + Vector = Point'''
        #assert(type(vector) == Vector)
        newPoint = (self.point[0]+vector.vec[0], \
                  self.point[1]+vector.vec[1], \
                  self.point[2]+vector.vec[2])
        return Point(newPoint)

    @property
    def x(self):
        return self.point[0]
    
    @property
    def y(self):
        return self.point[1]
    
    @property
    def z(self):
        return self.point[2]

if __name__ == '__main__':
    
    print "Führe Tests aus..."
    
    p1 = Point(1,2,3)
    p2 = Point(2,2,2)

    # Subtraktion testen
    assert(p1-p2 == Vector(-1,0,1))

    # Addition testen
    assert(p1+Vector(1,-2,1.5) == Point(2,0,4.5))
    
    print "Alle Tests erfolgreich"
