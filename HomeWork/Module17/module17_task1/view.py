def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '*'))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('Доступные действия:\n'
              '1. Добавить новую пару\n'
              '2. Отобразить всю обувь\n'
              '3. Найти пару\n'
              '4. Удалить пару\n'
              'Выход. Завершить программу')
        query = input('Введите номер действия: ')
        return query

    @add_title('Добавление новой статьи')
    def add_new_shoe(self):
        dict_shoe = {'Вид обуви': None,
                     'Тип обуви (муж/жен)': None,
                     'Цвет': None,
                     'Price': None,
                     'Производитель': None,
                     'Размер': None
                     }
        for key in dict_shoe.keys():
            dict_shoe[key] = input(f'Введите {key.lower()} обуви: ')
        return dict_shoe

    @staticmethod
    def __throw_an_error__(error):
        print('Произошла какая-то ошибка:', error)

    @staticmethod
    def print_shoes(shoe):
        if shoe:
            [print(f'{i}. {shoe}') for i, shoe in enumerate(shoe, 1)]
        else:
            print('Не найдено ни одной пары обуви')

    @staticmethod
    def find_shoes():
        manuf = input('Введите производителя для поиска: ')
        return manuf

    @staticmethod
    def remove_by_num():
        number = int(input('Введите номер пары для удаления: '))
        return number

    @staticmethod
    def remove_by_manuf():
        manufacturer = input('Введите производителя для удаления: ')
        return manufacturer

    @staticmethod
    def return_delete_result(result):
        print(result)
