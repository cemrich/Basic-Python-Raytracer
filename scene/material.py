from geometry import Vector


class Material(object):

    def __init__(self, color=None):
        '''color als Color'''
        self.color = color
        if not color:
            self.color = Color(128, 128, 128)


class Color(Vector):

    def __init__(self, r, g=0, b=0):
        Vector.__init__(self, r, g, b)

    def validate(self):
        return Color(tuple([255 if c > 255 else c for c in self.vec]))

    def __mul__(self, other):
        return super(Color, self).__mul__(other)

    def __add__(self, other):
        return super(Color, self).__add__(other)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def toHexString(self):
        return '#%02X%02X%02X' % (self.r, self.g, self.b)
