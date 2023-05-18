def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '*'))
            result = func(*args, **kwargs)
            print('*' * 50)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def get_user_command(self):
        print('1. Добавить обувь\n'
              '2. Показ всех моделей\n'
              '3. Найти обувь\n'
              '4. Удалить пару\n'
              '0. Exit the program')
        result = input('Выберите команду: ')
        return result

    def add_new_shoe(self):
        dict_shoe = {'Вид обуви': None,
                     'Производитель': None,
                     'Тип обуви (муж/жен)': None,
                     'Цвет': None,
                     'Размер': None,
                     'Цена': None}
        for key in dict_shoe.keys():
            dict_shoe[key] = input(f'Введите {key.lower()} обуви: ')
        return dict_shoe

    def __throw_an_error__(self, error):
        print('Произошла какая-то ошибка:', error)

    # def print_shoes(self, shoes):
    #     if shoes:
    #         [print(i + 1, shoe) for i, shoe in enumerate in enumerate(shoes)]
    #     else:
    #         print('Не найдено ни одной пары обуви')
    #
    # def find_shoes(self):
    #     manuf = input('Введите производителя для поиска: ')
    #     return manuf
    #
    # def get_article_name(self):
    #     type_shoe = input('Введите вид обуви для удаления')
    #     return type_shoe
    #
    # def get_deletion_context(self):
    #     number = int(input('Введите номер пары для удаления: '))
    #     return number
    #
    # def remove_shoe(self):
    #     manufacturer = input('Введите производителя для удаления: ')
    #     return manufacturer
    #
    # def return_delete_result(self, result):
    #     print(result)
