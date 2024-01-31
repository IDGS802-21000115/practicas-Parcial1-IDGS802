import math


class puntos():
    #declaracion de propiedades
    x1=0.0
    x2=0.0
    y1=0.0
    y2=0.0
    #declaracion de constructor
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def puntos(self):
        resultado= math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        return resultado
       
