import math


class CalcularsignoZodiacal():
    #declaracion de propiedades
    img=""
    nombre=""
    Apaterno=""
    Amaterno=""
    dia=""
    mes=""
    anio=""
    sexo=""
    resultado=""
    #declaracion de constructor
    def __init__(self,nombre,Apaterno,Amaterno,dia,mes,anio):
        self.nombre=nombre
        self.Apaterno=Apaterno
        self.Amaterno=Amaterno
        self.dia=dia
        self.mes=mes
        self.anio=anio
        
    def signo(self):
         fecha_actual = (2024, 2, 9)
         edad = fecha_actual[0] - int(self.anio) - ((fecha_actual[1], fecha_actual[2]) < (int(self.mes), int(self.dia)))
         if self.anio==2014 or self.anio==2002 or self.anio==1990 or self.anio==1978 or self.anio==1966:
          img="static/bootstrap/img/caballo.PNG"
          return ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+ " Tienes "+ str(edad)+ " años y eres un caballo " ,img]
         else:
          if self.anio==2015 or self.anio==2003 or self.anio==1991 or self.anio==1979 or self.anio==1967:
           img="static/bootstrap/img/cabra.PNG"
           return ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+ " Tienes "+ str(edad)+ " años y eres una cabra" ,img]
          else:
             if self.anio==2016 or self.anio==2004 or self.anio==1992 or self.anio==1980 or self.anio==1968:
               img="static/bootstrap/img/chango.PNG"
               return ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un mono",img]
             else:
                if self.anio==2017 or self.anio==2005 or self.anio==1993 or self.anio==1981 or self.anio==1969:
                 img="static/bootstrap/img/gallo.PNG"
                 return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un gallo",img]
                else:
                   if self.anio==2018 or self.anio==2006 or self.anio==1994 or self.anio==1982 or self.anio==1970:
                    img="static/bootstrap/img/perro.PNG"
                    return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un perro",img]
                   else:
                      if self.anio==1959 or self.anio==2007 or self.anio==1995 or self.anio==1983 or self.anio==1971:
                       img="static/bootstrap/img/perco.PNG"
                       return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un cerdo",img]
                      else:
                        if self.anio==2008 or self.anio==1996 or self.anio==1984 or self.anio==1972 or self.anio==1960:
                         img="static/bootstrap/img/raton.PNG"
                         return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres una rata",img]
                        else:
                          if self.anio==2009 or self.anio==1997 or self.anio==1985 or self.anio==1973 or self.anio==1961:
                           img="static/bootstrap/img/toro.PNG"
                           return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un Buey",img]
                          else:
                            if self.anio==2010 or self.anio==1998 or self.anio==1986 or self.anio==1974 or self.anio==1962:
                             img="static/bootstrap/img/tigre.PNG"
                             return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un Tigre",img]
                            else:
                              if self.anio==2011 or self.anio==1999 or self.anio==1987 or self.anio==1975 or self.anio==1963:
                               img="static/bootstrap/img/conejo.PNG"
                               return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un conejo",img]
                              else:
                                if self.anio==2012 or self.anio==2000 or self.anio==1988 or self.anio==1976 or self.anio==1964:
                                 img="static/bootstrap/img/dragon.PNG"
                                 return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+" Tienes "+ str(edad)+ " años y eres un Dragon",img]
                                else:
                                  if self.anio==2013 or self.anio==2001 or self.anio==1989 or self.anio==1977 or self.anio==1965:
                                    img="static/bootstrap/img/serpiente.PNG"
                                    return  ["Hola "+self.nombre +" "+ self.Apaterno +" " + self.Amaterno+ " Tienes "+ str(edad)+ " años y eres una serpiente",img]
                                  else:
                                   return"fecha no valida"


                         

       
