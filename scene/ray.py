# -*- coding: utf-8 -*-

class Ray(object):
    '''
    Strahl im Raum mit einem Ursprung und einer
    (normalisierten) Richtung.
    '''
    
    def __init__(self, origin, direction):
        '''
        @param origin:    Ausgangspunkt des Strahls
        @param direction: Richtung, in die der Strahl zeigt
        '''
        self.origin = origin # point
        self.direction = direction.normalized() # vector

    def __repr__(self):
        return 'Ray(%s,%s)' % (repr(self.origin), repr(self.direction))

    def pointAtParameter(self, distance):
        '''
        @param t: Skalierungsfaktor für die Richtung
        @return:  Punkt auf dem Strahl mit dem Abstand distance vom Ausgangspunkt
        '''
        return self.origin + self.direction.scale(distance)
