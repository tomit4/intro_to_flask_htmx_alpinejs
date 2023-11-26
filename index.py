from flask import Flask, get_flashed_messages, render_template, request, flash, redirect, url_for
from dotenv import dotenv_values, load_dotenv
import json

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
    '''
        NOTE: This json.dumps is counter-intuitive as we're 
        looking to return HTML, but sqlite returns raw data 
        not in JSON or XML style format. 
        (Jinja does transpilation under the hood?)
    '''
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    posts = json.dumps([dict(post) for post in posts])
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


# NOTE: Notice how flask expresses url string params
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
