"""
Running this app locally, make sure the data file is imported correctly.

Like so - from web_app.data import data.
Changed to - from II.web_app.data import data - only for DispatcherMiddleware stuff.
"""

from flask import Flask, render_template, request, redirect, url_for
from II.web_app.data import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/autorius_sarasas")
def list():
    return render_template("list.html", data=data)


@app.route("/<string:title>")
def article(title):
    return render_template("article.html", title=title, data=data)


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    if request.method == "POST":
        date = request.form["date"]
        autorius = request.form["autorius"]
        tekstas = request.form["tekstas"]
        pavadinimas = request.form["pavadinimas"]
        data.append(
            {
                "data": date,
                "autorius": autorius,
                "pavadinimas": pavadinimas,
                "tekstas": tekstas,
                "status": "published",
            }
        )
        return redirect(url_for("list"))
    return render_template("add_article.html")


if __name__ == "__main__":
    app.run(debug=True)
