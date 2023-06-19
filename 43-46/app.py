import sqlite3
import os

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g

from DataBase import DataBase


DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '73d2834775852cd9336ce9abbe19c875883e2e54'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'О нас', 'url': '/about'},
    {'name': 'Обратная связь', 'url': '/contacts'}
]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    dbase = DataBase(db)
    return render_template('index.html', title='Главная', menu=dbase.get_menu())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = DataBase(db)

    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['text']) > 10:
            res = dbase.add_post(request.form['title'], request.form['text'])
            if res:
                flash('Статья добавлена успешно!', category='success')
            else:
                flash('Ошибка добавления статьи!', category='error')
        else:
            flash('Ошибка добавления статьи!', category='error')
    return render_template('add_post.html', title='Добавление статьи', menu=dbase.get_menu())


@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/contacts', methods=['POST', 'GET'])
def contacts():
    if request.method == 'POST':
        if len(request.form['username']) > 1:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки!', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message'],
        # }
        # return render_template('contacts.html', **context, title='Обратная связь', menu=menu)

    return render_template('contacts.html', title='Обратная связь', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь {username}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'ivan' \
                                  and request.form['password'] == '1234':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


if __name__ == '__main__':
    app.run()
