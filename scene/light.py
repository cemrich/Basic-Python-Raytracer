
class Light(object):

    def __init__(self, position, intensity=1):
        '''
        position: position der Lichtquelle (Point)
        intensity: wie intensiv ist die Lichtquelle (0-1)
        '''
        self.position = position
        self.intensity = intensity

    def intersect(self, ray):
        pass
