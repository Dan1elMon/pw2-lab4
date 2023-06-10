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
    contador = len(self.img)-1;
    #print (contador)
    for i in range(len(self.img)):
        vertical.append(self.img[contador])
        contador=contador-1

    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    
    def invertirString(cadena):
      strInvertido=""
      for caracter  in cadena:
          strInvertido = caracter + strInvertido
      return strInvertido
    
    figura= []
    for text in self.img:
        figura.append(invertirString(text))
    return Picture(figura)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    #cambiarCaracteres cambia caracter de cualquier cadena. en este caso cambiamamos los caracteres  de cada
    #elemento de la lista del objeto picture , para eso usamos join que une todo los caracteres vacios devolviendo nuevamente
    #un string. Interesante la manera como el join reconoce como un objeto iterable al for entre  corchetes
    cambiarCaracteres =  lambda cadena : "".join([self._invColor(cadena[i]) for  i  in range(len(cadena))])
    figura=[]
    for text in self.img:
      figura.append(cambiarCaracteres(text))
    return Picture(figura)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    figura= []
    for i in range(len(self.img)):
        figura.append(self.img[i]+p.img[i])

    return Picture(figura)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    figura= p.img
    for text in self.img:
      figura.append(text)
    return Picture(figura)
   # return Picture(None)

  def under(self, p):
    def cambiar(caracter1,caracter2):
        if caracter2 == " ":
            return caracter1
        else :
            return caracter2
    #mismo join aplicando a un for entre corchetes
    unirCaracter =  lambda cadena1,cadena2 : "".join([cambiar(cadena1[i],cadena2[i]) for  i  in range(len(cadena1))])
    figura= []
    for i in range(len(self.img)):
        figura.append(unirCaracter(self.img[i],p.img[i]))
    return Picture(figura)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    figura= []
    for text in self.img:
        aux = ""   
        for j in range(n-1):
            aux+= text
        figura.append(aux)
    return Picture(figura)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual abajo
      la cantidad de veces que indique el valor de n """
    figura= []
    for i in range(n):
      for t in self.img:
        figura.append(t)
    return Picture(figura)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    figura= []
    text= ""
    for c in range(len(self.img[0])):
      for t in self.img:
        text+= t[c]
      figura.append(text)
      text= ""
    return Picture(figura)
