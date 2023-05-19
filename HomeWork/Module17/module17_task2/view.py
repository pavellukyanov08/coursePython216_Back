class View:
    @staticmethod
    def get_user_command():
        print('Доступные действия:\n'
              '1. Добавить новый рецепт\n'
              '2. Отобразить рецепты\n'
              '3. Поиск рецепта\n'
              '4. Удалить рецепт\n'
              'Выход. Завершить программу')
        query = input('Введите номер действия: ')
        return query

    @staticmethod
    def get_recipe_data():
        properties = ['name', 'author', 'type_recipe', 'description', 'yt_link', 'lst_ingred', 'type_kitchen']
        data = [input(f'Введите {prop}: ') for prop in properties]
        return data

    @staticmethod
    def find_recipe():
        name = input('Введите название рецепта для поиска: ')
        return name

    @staticmethod
    def print_recipe(recipe):
        [print(f'{i}. {recipe}') for i, recipe in enumerate(recipe, 1)]

    def remove_recipe(self, recipes):
        self.print_recipe(recipes)
        number = int(input('Введите номер рецепта, который нужно удалить: '))
        return number
