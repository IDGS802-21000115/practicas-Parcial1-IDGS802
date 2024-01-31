from flask import Flask, render_template,request
from CalcularDistacia import puntos
import forms
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

if __name__ == "__main__":
    app.run(debug=True)
