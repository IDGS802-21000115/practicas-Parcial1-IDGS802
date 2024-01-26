from flask import Flask, render_template,request
 
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
    

if __name__ == "__main__":
    app.run(debug=True)
