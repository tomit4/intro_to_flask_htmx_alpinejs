from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import dotenv_values, load_dotenv

load_dotenv()
from flask_cors import CORS
import sqlite3

app = Flask(__name__, static_folder='public')
app.config['SECRET_KEY'] = dotenv_values('.env')['SECRET']
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


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


#  @app.route('/')
#  @app.route('/name')
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
