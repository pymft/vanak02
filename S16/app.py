from flask import Flask, render_template, request

#
app = Flask("my app")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        w = request.form['w']
        h = request.form['h']
        bmi = float(w) / (float(h)**2)

        return render_template("index.html", bmi=bmi)


# 10.10.204.241:8080
# sqlalchemy
app.run(port=8080, host='0.0.0.0')
