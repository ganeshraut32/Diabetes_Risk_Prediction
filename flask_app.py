# app.py
from flask import Flask, render_template, request
from model import regressor_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Diebetic_view():
    if request.method == 'GET':
        return render_template("colorful_form_diabetic.html")
    elif request.method == 'POST':
        glucose = float(request.form["glucose"])
        BP = float(request.form["BP"])
        ST = float(request.form["ST"])
        Insuline = float(request.form["Insuline"])
        BMI = float(request.form["BMI"])
        Preg= float(request.form["Preg"])
        Age = float(request.form["Age"])
        DPF = float(request.form["DPF"])

        op_array = regressor_model.predict([[glucose,BP,ST,Insuline,BMI,Preg,Age,DPF]])
        y_pred = round(op_array[0], 2)
        return render_template("output.html", predicted_price=y_pred)

if __name__ == '__main__':
    app.run(debug=True)