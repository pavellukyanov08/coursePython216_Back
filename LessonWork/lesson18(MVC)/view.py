def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '-'))
            result = func(*args, **kwargs)
            print('-'*50)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('-'*50)
        print('Ожидание пользовательского ввода: '.center(50, '='))
        print('Доступные действия:\n'
              '1. Добавить новую статью: ',
              '2. Отобразить все статьи: ',
              '3. Найти статьи: ',
              '4. : ')
        print('-' * 50)
        query = input('Введите команду: ')
        return query

    @add_title('Ожидание пользовательского ввода')
    def add_new_article(self):
        dict_article = {'Название': None,
                        'Автор': None,
                        'Кол-во знаков': None,
                        'Издательство': None,
                        'Аннотация': None,
                        }

        for key in dict_article.keys():
            dict_article[key] = input(f'Введите {key.lower()} статью')
        return dict_article

    @add_title('Неизвестная ошибка')
    def __throw_an_error__(self, error):
        print('Произошла какая-то ошибка', error)

    @add_title('Список статей')
    def print_articles(self, articles):
        if articles:
            [print(articles) for articles in articles]
        else:
            print('Ни одной статьи нет')

    @add_title('Поиск статей')
    def find_article(self):
        criteria = input('Введите список слов для поиска через пробел').split()
        return criteria

    @add_title('Название статей')
    def get_article_name(self):
        name = input('Введите название статье для удаления')
        return name

    @add_title('Список статей')
    def print_articles(self, articles):
        if articles:
            [print(i + 1, article) for i, article in enumerate(articles)]
        else:
            print('Ни одной статьи нет!')

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер статьи'))
        return number
