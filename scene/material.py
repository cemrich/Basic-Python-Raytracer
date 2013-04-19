# -*- coding: utf-8 -*-

from geometry import Vector
import math

class Material(object):

    def __init__(self, ambientColor=None, diffuseColor=None, specularColor=None, glossiness=0.1):
        '''
        ambientColor:  Basis-Farbe (auch im Schatten); default = grau
        diffuseColor:  Farbe für den diffusen Anteil (abhängig von Lichtquelle); default = ambientColor
        specularColor: Farbe für die Highlights; default = weiß * glossiness
        glossiness:    Spiegeleigenschaft; 0 = matt, 1 = perfekter Spiegel; default = 0.1
        '''
        
        # Default-Farben setzen, wenn nicht übergeben
        self.ambientColor = ambientColor if ambientColor else GRAY
        self.diffuseColor = diffuseColor if diffuseColor else self.ambientColor
        self.specularColor = specularColor if specularColor else Color(glossiness, glossiness, glossiness)
        
        self.glossiness = glossiness
        self.n = 64 * glossiness + 1                        # < 32 = rau, > 32 = glatt, unedlich = perfekter Spiegel 
        self.specConst = (self.n + 2) / (math.pi * 2)       # Normalisierungsfaktor (siehe http://de.wikipedia.org/wiki/Phong-Beleuchtungsmodell)
        
        self.baseLight = self.ambientColor * AMBIENT_COLOR  # caching for performance
    
    def baseColorAt(self, point):
        return self.baseLight
    
    def renderColor(self, lightRay, normal, lightColor, rayDirection):
        '''
        Gibt die Farbe dieses Materials für eine bestimmte Lichtqualität zurück.
        @param lightRay: Strahl vom zu rendernden Punkt zur Lichtquelle (Ray)
        @param normal: Normale an der zu rendernden Stelle (Vector)
        @param lightColor: Farbe der Lichtquelle
        @param rayDirection: Blickrichtung auf die zu rendernde Stelle (Vector)
        @return: Farbe dieses Materials (Color)
        '''
        color = BLACK
        diffuseFactor = lightRay.direction.dot(normal)
    
        if diffuseFactor > 0:
            color += self.diffuseColor * lightColor * diffuseFactor
            reflectedLight = (lightRay.direction).reflect(normal)
            specularFactor = reflectedLight.dot(-rayDirection)
            if specularFactor > 0:
                color += self.specularColor * lightColor * (specularFactor**self.n) * self.specConst
        return color

class CheckedMaterial(object):
    
    def __init__(self):
        self.whiteMat = Material(Color(0.5, 0.5, 1), WHITE, glossiness=0.3)
        self.blackMat = Material(BLACK, Color(0, 0, 0.1), WHITE, glossiness=0.05)
        self.currMat = self.whiteMat
        
    def baseColorAt(self, point):
        xMod = point.x % 4
        zMod = point.z % 4
        if (xMod > 2 and zMod > 2) or (xMod <= 2 and zMod <= 2):
            self.currMat = self.whiteMat
        else:
            self.currMat = self.blackMat
            
        return self.currMat.baseColorAt(point)
        
    def renderColor(self, lightRay, normal, lightColor, rayDirection):
        return self.currMat.renderColor(lightRay, normal, lightColor, rayDirection)

    @property
    def glossiness(self):
        return self.currMat.glossiness

class Color(Vector):
    '''
	Farbe als dreidimensionaler Vektor, der die Rot-, Grün
	und Blau-Werte abbildet. Alle Werte sind zwischen 0 und
	1 normalisiert.
	'''

    def __init__(self, r, g=0, b=0):
        Vector.__init__(self, r, g, b)

    def __mul__(self, other):
        return super(Color, self).__mul__(other)

    def __add__(self, other):
        return super(Color, self).__add__(other)

    def toValidatedHexString(self):
        self.vec = tuple([1 if c > 1 else c for c in self.vec])
        return '#%02X%02X%02X' % (self.vec[0] * 255, self.vec[1] * 255, self.vec[2] * 255)

BLACK = Color(0, 0, 0)
GRAY = Color(0.5, 0.5, 0.5)
WHITE = Color(1, 1, 1)

AMBIENT_COLOR = Color(0.3, 0.3, 0.3)