from flask import Flask, render_template,request
from CalcularDistacia import puntos
import forms
from guaradadopalabras import Guardar
from oroscopo import CalcularsignoZodiacal
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/formulario",methods=["GET","POST"])
def calculo():
     return render_template("formulario1.html")


@app.route("/resultado",methods=["GET","POST"])
def calculacion():

 if request.method=="POST":
    calculo_seleccionada = request.form.get("operaciones")
    if calculo_seleccionada=="multiplicacion":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        r=int(num1)*int(num2)
        
        return render_template("formulario1.html",r=r)
    else:
        if calculo_seleccionada=="suma":
       
          num1=request.form.get("n1")
          num2=request.form.get("n2")
          r=int(num1)+int(num2)
          return render_template("formulario1.html",r=r)
        else:
         if calculo_seleccionada=="resta": 
            
              num1=request.form.get("n1")
              num2=request.form.get("n2")
              r=int(num1)-int(num2)
              return render_template("formulario1.html",r=r)
         else:
            if calculo_seleccionada=="division": 
                 
                 num1=request.form.get("n1")
                 num2=request.form.get("n2")
                 r=float(num1)//float(num2)
                 return render_template("formulario1.html",r=r)
    
@app.route("/DistanciaPuntos",methods=["GET","POST"])
def calculoPuntos():
    x1=0.0
    x2=0.0
    y1=0.0
    y2=0.0
    form=forms.UserForm(request.form)
    if request.method == "POST":
        x1 = float(form.x1.data)
        x2 = float(form.x2.data)
        y1 = float(form.y1.data)
        y2 = float(form.y2.data)
    r=puntos(x1,x2,y1,y2)
    result=r.puntos()
    return render_template("formulaPuntos.html", form=form, result=result)
@app.route("/oroscopo",methods=["GET","POST"])
def oro():
    form=forms.UserForm(request.form)
    return render_template("formularioOroscopo.html", form=form)

@app.route("/resultadoOro",methods=["GET","POST"])
def calculoResistencias():
    nombre=""
    Apaterno=""
    Amaterno=""
    dia=""
    mes=""
    anio=""
    
    form=forms.UserForm(request.form)
    if request.method == "POST":
        nombre = form.nombre.data
        Apaterno = form.Apaterno.data
        Amaterno = form.Amaterno.data
        dia = int(form.dia.data)
        mes = int(form.mes.data)
        anio =int(form.anio.data)
    
    r=CalcularsignoZodiacal(nombre,Apaterno,Amaterno,dia,mes,anio)
    result=r.signo()
    result2=result[0]
    img=result[1]
    return render_template("formulaOro2.html", form=form, result=result2, img=img)


@app.route("/guardarPalabras",methods=["GET","POST"])
def diccionario():
    palabra_Ingles=""
    palabra_Español=""
    pal=""
    palabra=""
    
    form=forms.UserForm(request.form)
    if request.method == "POST":
        palabra_Ingles = form.palabra_Ingles.data
        palabra_Español = form.palabra_Español.data
        pal=form.pal.data
        palabra=form.palabra.data
    r=Guardar(palabra_Ingles,palabra_Español,pal,palabra)
    result = r.buscar() or ""
    
    result2 = r.apalabra() or ""
    
    return render_template("diccionario.html", form=form, result=result, result2=result2)

if __name__ == "__main__":
    app.run(debug=True)
