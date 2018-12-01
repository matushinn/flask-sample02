from flask import Flask, render_template
import random

app = Flask(__name__)

items = ["大吉","吉","中吉","小吉","大凶"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html",name=name)

@app.route("/omikuji/<name>")
def omikuji(name):
    item=random.choice(items)
    return render_template("omikuji.html",item=item,name=name)



if __name__ == "__main__":
    app.run(debug=True)
