from flask import Flask, render_template
import calendar

app = Flask(__name__)


@app.route("/")
def leap():
    return render_template("leap.html", calendar=calendar)


if __name__ == "__main__":
    app.run(debug=True)
