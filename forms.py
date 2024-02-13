from wtforms import Form, RadioField
from wtforms import StringField

 
class UserForm(Form):
    x1 = StringField("x1")
    y1 = StringField("y1")
    x2 = StringField("x2")
    y2 = StringField("y2")
    nombre = StringField("nombre")
    Apaterno = StringField("Apaterno")
    Amaterno = StringField("Amaterno")
    dia = StringField("dia")
    mes = StringField("mes")
    anio = StringField("anio")
    radios = RadioField('Sexo',choices=[("mujer", "Femenino"),("Hombre", "Masculino")])