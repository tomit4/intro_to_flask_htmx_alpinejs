from flask import Flask, render_template, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__, static_folder='public')
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    if request.method == 'GET':
        return render_template('get_example.html', posts=posts)


#  @app.route('/')
#  @app.route('/<name>')
#  def index(name=None):
#  return render_template("index.html", name=name)

#  @app.route('/user')
#  def user(user_id):
#  if request.method == 'POST':
#  if request.method == 'DELETE'
#  if request.method == 'PUT'
#  if request.method == 'PATCH'
#  if request.method == 'DELETE'

if '__main__':
    app.run(debug=True)
