from material import Material


class Triangle(object):

    def __init__(self, p1, p2, p3, material=None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.u = p2 - p1
        self.v = p3 - p1
        self.normal = self.u.cross(self.v).normalized()

        self.material = material if material else Material()

    def __repr__(self):
        return "Triangle(%s, %s, %s)" % (repr(self.p1), repr(self.p2), repr(self.p3))

    def intersectionParameter(self, ray):
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
        return self.normal
