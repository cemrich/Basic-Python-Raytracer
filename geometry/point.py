# -*- coding: utf-8 -*-
import math
from vector import Vector

class Point(object):
    def __init__(self, point, y=0, z=0):
        if (type(point) == tuple):
            self.point = point
        else:
            self.point = (point, y, z)
        self.point = tuple(map(float, self.point))

    def __repr__(self):
        return 'Point(%s, %s, %s)' % (repr(self.point[0]), repr(self.point[1]), repr(self.point[2]))

    def __eq__(self, otherPoint):
        return self.point == otherPoint.point

    def __sub__(self, otherPoint):
        '''Point - Point = Vector'''
        assert(type(otherPoint) == Point)
        newVec = tuple(map(lambda coords: coords[0]-coords[1], zip(self.point, otherPoint.point)))
        return Vector(newVec)

    def __add__(self, vector):
        '''Point + Vector = Point'''
        assert(type(vector) == Vector)
        newPoint = tuple(map(lambda coords: coords[0]+coords[1], zip(self.point, vector.vec)))
        return Point(newPoint)

if __name__ == '__main__':
    
    p1 = Point(1,2,3)
    p2 = Point(2,2,2)

    # Subtraktion testen
    assert(p1-p2 == Vector(-1,0,1))
