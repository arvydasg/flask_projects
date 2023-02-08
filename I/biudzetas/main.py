import os
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


# if __name__ == "__main__":
#     from models.irasas import Irasas

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "biudzetas.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.app_context().push()  # this line solves "runtimeerror: working outside of application context python" error
db.create_all()


@app.route("/prideti", methods=["GET", "POST"])
def prideti():
    if request.method == "POST":
        suma = request.form["suma"]
        info = request.form["info"]
        irasas = Irasas(suma, info)
        db.session.add(irasas)
        db.session.commit()
        return sarasas()
    elif request.method == "GET":
        return render_template("prideti.html")


@app.route("/")
def sarasas():
    biudzetas = Irasas.query.all()
    return render_template("sarasas.html", biudzetas=biudzetas)


@app.route("/balansas")
def balansas():
    biudzetas = db.session.query(Irasas).all()
    balansas = 0
    for irasas in biudzetas:
        balansas += irasas.suma
    return render_template("balansas.html", balansas=balansas)


@app.route("/biudzetas/irasas_delete/<int:id>")
def irasas_delete(id):
    uzklausa = db.session.query(Irasas).get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for("sarasas"))


@app.route("/biudzetas/irasas_update/<int:id>", methods=["GET", "POST"])
def irasas_update(id):
    if request.method == "POST":
        irasas = db.session.query(Irasas).get(id)
        irasas.suma = request.form["suma"]
        irasas.info = request.form["info"]
        db.session.commit()
        return redirect(url_for("sarasas"))
    elif request.method == "GET":
        irasas = db.session.query(Irasas).get(id)
        return render_template("redaguoti.html", irasas=irasas)


class Irasas(db.Model):
    __tablename__ = "Irasas"
    id = db.Column(db.Integer, primary_key=True)
    suma = db.Column("Suma", db.Float)
    info = db.Column("Info", db.String(120))

    def __init__(self, suma, info):
        self.suma = suma
        self.info = info

    def __repr__(self):
        return f"{self.id}: suma - {self.suma}, info - {self.info}"


db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
