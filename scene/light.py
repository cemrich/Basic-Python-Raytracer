# -*- coding: utf-8 -*-

from material import WHITE

class Light(object):

    def __init__(self, position, color=WHITE):
        '''
        position: position der Lichtquelle (Point)
        color: Farbe des Lichtes (default weiß)
        '''
        self.position = position
        self.color = color
