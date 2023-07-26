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


menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'Об авторе', 'url': 'about'}
]


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('index.html', title='Главная',
                           menu=db.get_menu())


@app.route('/photos')
def photos():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('photos.html', title='Фото',
                           menu=db.get_menu(),
                           photo=db.get_photos())


@app.route('/about')
def about():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('about.html', title='Об авторе', menu=db.get_menu())


if __name__ == '__main__':
    create_db()
    app.run()
