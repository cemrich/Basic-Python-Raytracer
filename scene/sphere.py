import math

class Sphere(object):
    def __init__(self, center, radius):
        self.center = center # point
        self.radius = radius # scalar

        self.material = Material(0, 255, 0)

        print "Kugel initialisiert:", repr(self)

    def __repr__(self):
        return 'Sphere(%s,%s)' % (repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v**2 - co.dot(co) + self.radius**2
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        return (p - self.center).normalized()


class Material(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
        
