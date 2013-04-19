# -*- coding: utf-8 -*-

from material import WHITE

class Light(object):
    '''
    Einfache Punktlichtquelle mit optional farbigem Licht.
    '''

    def __init__(self, position, color=WHITE):
        '''
        @param position:  Position der Lichtquelle (Point)
        @param color:     Farbe des Lichtes (default weiß)
        '''
        self.position = position
        self.color = color
