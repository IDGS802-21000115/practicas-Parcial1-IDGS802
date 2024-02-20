from wtforms import Form, RadioField
from wtforms import StringField
from wtforms import validators
 
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
    palabra_Ingles=StringField('palabra_Ingles',[validators.DataRequired(message='el campo es requerido')])
    palabra_Español=StringField('palabra_Español',[validators.DataRequired(message='el campo es requerido')])
    pal = RadioField('Palabra',choices=[("ingles", "palabra_Ingles"),("español", "palabra_Español")])
    palabra=StringField('palabra')