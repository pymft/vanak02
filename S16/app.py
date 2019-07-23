from flask import Flask, render_template

#
app = Flask("my app")


@app.route('/')
@app.route('/<int:rows>/<int:cols>')
def index(rows=100, cols=100):
    return render_template("index.html", rows=rows, cols=cols)


@app.route('/login')
def login():
    with open("./templates/login.html") as f:
        text = f.read()
    return text


@app.route("/greeting/<name>")
def greeting(name):
    with open("./templates/greeting.html") as f:
        text = f.read()
    return text.format(name=name)


app.run(port=8080)
