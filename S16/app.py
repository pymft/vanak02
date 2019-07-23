from flask import Flask, render_template

#
app = Flask("my app")


@app.route('/')
@app.route('/<int:rows>/<int:cols>')
def index(rows=100, cols=100):
    return render_template("index.html", rows=rows, cols=cols)




app.run(port=8080)
