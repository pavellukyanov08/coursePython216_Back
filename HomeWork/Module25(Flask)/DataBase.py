import sqlite3 as sq
import os


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения данных')
        return []

    def get_menu(self):
        return self._get_objects('menu')

    def get_photos(self):
        return self._get_objects('photos')

    def get_posts(self):
        return self._get_objects('posts')

    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT title, text, description FROM posts WHERE url == "{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sq.Error as e:
            print('Ошибка получения данных о посте', e)
        return None, None

    def add_post(self, url, title, text, description):
        try:
            self.__cur.execute(f'SELECT count() as "count" FROM posts WHERE url == "{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Такой пост уже существует!')
                return False

            self.__cur.execute('INSERT INTO posts VALUES (NULL, ?, ?, ?, ?)',
                               (url, title, text, description))
            self.__db.commit()
        except sq.Error as e:
            print('Ошибка добавления статью в БД', e)
            return False
        return True

    def add_photo(self):
        try:
            thumbnail_folder_path = 'static/img/thumbnail'
            for thumbnail in os.listdir(thumbnail_folder_path):
                if thumbnail.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.__cur.execute(f'INSERT INTO photos VALUES (null, ?)', (thumbnail,))
                    self.__db.commit()
            return True
        except IOError as e:
            print('Ошибка добавления в базу', e)
            return False



