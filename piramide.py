

class piramide():
    #declaracion de propiedades
    x=0
    #declaracion de constructor
    def __init__(self,xx):
        self.x=xx
    def arbol(self):
        i = 1
        while i <= self.x:
            i2=1
            while i2<=i:
             astediscos = "*"*(i2)
             i2 +=1
            print(astediscos)
            i += 1
def main(): 
      x=int(input("dame el valor del tamaño de tu arbol"))
      x2=piramide(x)
      x2.arbol() 
if __name__=="__main__":
    main()
   