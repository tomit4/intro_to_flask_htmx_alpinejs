from flask import Flask, render_template

app = Flask(__name__, static_folder='public')


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template("index.html", name=name)


if '__main__':
    app.run(debug=True)
