

from io import open


class Guardar():
    #declaracion de propiedades
    palabra_Ingles=""
    palbra_Español=""
    pal=""
    palabra=""
    
    #declaracion de constructor
    def __init__(self,palabra_Ingles,palabra_Español,pal,palabra):
        self.palabra_Ingles=palabra_Ingles
        self.palabra_Español=palabra_Español
        self.palabra=palabra
        self.pal=pal
    def apalabra(self):
     try:
        archivo_texto = open('nombres.txt', 'a')
        archivo_texto.write('\n' + self.palabra_Español + '-' + self.palabra_Ingles)
        archivo_texto.close()
        return "¡Muy bien insertado correctamente!"
     except Exception as e:
        return f"Error al insertar la palabra: {e}"
         
    def buscar(self):
        with open('nombres.txt', 'r') as archivo_texto:
            for linea in archivo_texto:
                palabras = linea.strip().split('-')
                
                if len(palabras) == 2:
                    palabra_espanol, palabra_ingles = palabras
                    
                    if self.pal == "español" and (palabra_espanol.lower() == self.palabra.lower() or palabra_ingles.lower()== self.palabra.lower()):
                        respu=f"Palabra en español para {self.palabra} es {palabra_espanol}"
                        return respu
                    elif self.pal == "ingles" and (palabra_ingles.lower() == self.palabra.lower() or palabra_espanol.lower() == self.palabra.lower()):
                        respu2=f"Palabra en ingles para {self.palabra} es {palabra_ingles}"
                        return respu2
            return f"No se encontró la palabra '{self.palabra}' en el idioma '{self.pal}'."
      