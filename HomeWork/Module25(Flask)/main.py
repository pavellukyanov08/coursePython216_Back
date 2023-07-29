import os.path
import sqlite3

from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
from DataBase import DataBase

DATABASE = '/tmp/homework.db'
DEBUG = True
SECRET_KEY = '123zxcasdqwe'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({'DATABASE': os.path.join(app.root_path, 'homework.db')})


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


# menu = [
#     {'name': 'Главная', 'url': '/'},
#     {'name': 'Об авторе', 'url': 'about'}
# ]


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('index.html', title='Главная',
                           menu=db.get_menu(),
                           posts=db.get_posts())


@app.route('/post/<post_id>')
def show_post(post_id):
    db_con = connect_db()
    db = DataBase(db_con)

    title, text, description = db.get_post(post_id)
    if not title:
        abort(404)
    return render_template('post.html', title=title, text=text, description=description, menu=db.get_menu())


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    db_con = connect_db()
    db = DataBase(db_con)

    if request.method == 'POST':
        if len(request.form['title']) > 5 and len(request.form['text']) > 10 and len(request.form['description']) > 20:
            res = db.add_post(request.form['url'], request.form['title'],
                              request.form['text'], request.form['description'])
            if res:
                flash('Статья успешно добавлена!', category='success')
            else:
                flash('Ошибка добавления в статью!', category='error')
        else:
            flash('Ошибка добавления статьи!', category='error')

    return render_template('add_post.html', title='Добавление статьи', menu=db.get_menu())


@app.route('/photos')
def photos():
    db_con = connect_db()
    db = DataBase(db_con)
    # db.add_photo()
    return render_template('photos.html', title='Фото',
                           menu=db.get_menu(),
                           photos=db.get_photos())


@app.route('/about')
def about():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('about.html', title='Об авторе', menu=db.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('page404.html', title='Страница не найдена', menu=db.get_menu(), error=error), 404


if __name__ == '__main__':
    create_db()
    app.run()
