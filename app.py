from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/")
def predict():
    return render_template("index.html")

@app.route("/submit", methods = ['POST'])
def submit():
    if request.method == "POST":
        length = request.form['length']
        weight = request.form['weight']
        width = request.form['width']
        species = model.predict(weight, length, width)


    return render_template("submit.html", l=length, w=weight, wid=width, s=species)


if __name__ == "__main__":
    app.run(debug=False)