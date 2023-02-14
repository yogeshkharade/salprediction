from flask import Flask, redirect, request, render_template
import pickle
import numpy

app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template("info.html")

@app.route("/predict", methods=["post"])
def fun2():
    nm = request.form['name']
    exp = float(request.form['exp'])

    mymodel = pickle.load(open('Model_sal.pkl', 'rb'))
    sal =  round(mymodel.predict([[exp]])[0], 2)
    return "<h1> Hi {} <br/> Your Predicted Salary is {}".format(nm, sal)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    