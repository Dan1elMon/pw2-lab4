from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return vertical

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]
        return horizontal

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative = []
        for value in self.img:
            row = [_invColor(color) for color in value]
            negative.append(row)
        return negative

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        joined = []
        for i in range(len(self.img)):
            row = self.img[i] + p.img[i]
            joined.append(row)
        return joined

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return p.img + self.img

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return self.img + p.img
  
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repeated = []
        for row in self.img:
            repeated_row = []
            for _ in range(n):
                repeated_row.extend(row)
            repeated.append(repeated_row)
        return repeated

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        repeated = []
        for _ in range(n):
            repeated.extend(self.img)
        return repeated

    # Extra: Sólo para realmente viciosos 
    def rotate(self, clockwise=True):
        """ Devuelve una figura rotada en 90 grados en sentido horario o antihorario """
        rotated = []
        if clockwise:
            for j in range(len(self.img[0])):
                row = [self.img[i][j] for i in range(len(self.img)-1, -1, -1)]
                rotated.append(row)
        else:
            for j in range(len(self.img[0])-1, -1, -1):
                row = [self.img[i][j] for i in range(len(self.img))]
                rotated.append(row)
        return rotated