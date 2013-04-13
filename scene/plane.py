from material import Material


class Plane(object):

    def __init__(self, point, normal, material=None):
        self.point = point
        self.normal = normal.normalized()
        self.material = material if material else Material()

    def __repr__(self):
        return "Plane(%s, %s)" % (repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        op = ray.origin - self.point
        b = ray.direction.dot(self.normal)
        return -op.dot(self.normal) / b if b else None

    def normalAt(self, p):
        return self.normal
