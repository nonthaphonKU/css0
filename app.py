from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detail")
def detail():
    return render_template("/detail.html")

app.run(port=8000, debug=True)