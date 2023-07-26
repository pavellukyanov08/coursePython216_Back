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
        try:
            self.__cur.execute(f'SELECT photo FROM photos')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError as e:
            print('Ошибка чтения данных', e)
            return False

    def add_photo(self):
        try:
            # folder_path = 'static/img'
            # for image in os.listdir(folder_path):
            #     if image.lower().endswith(('.png', '.jpg', '.jpeg')):
            with open('static/img/photo_2x1.jpg', 'rb') as img_f:
                img_data = img_f.read()
                db_img = sq.Binary(img_data)
                # print(db_img)
                self.__cur.execute(f'''INSERT INTO photos VALUES (1, ?)''', db_img)
                self.__db.commit()

            # folder_path = 'static/img'
            # for image in os.listdir(folder_path):
            #     if image.lower().endswith(('.png', '.jpg', '.jpeg')):
            #         with open(os.path.join(folder_path, image), 'rb') as img_f:
            #             img_data = img_f.read()
            #             db_img = sq.Binary(img_data)
            #             print(db_img)
            #             self.__cur.execute(f'''INSERT INTO photos VALUES (1, ?)''', db_img)
            #             self.__db.commit()

            return True
        except IOError as e:
            print('Ошибка добавления в базу', e)
            return False



