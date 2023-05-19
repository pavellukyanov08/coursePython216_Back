from csv import reader, writer


class Recipe:
    def __init__(self, name, author, type_recipe, description, yt_link, lst_ingred, type_kitchen):
        self.name = name
        self.author = author
        self.type_recipe = type_recipe
        self.description = description
        self.yt_link = yt_link
        self.lst_ingred = lst_ingred
        self.type_kitchen = type_kitchen

    def __str__(self):
        return ', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.database = []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = reader(f)
                self.type_recipe = ['первое блюдо', 'второе блюдо']
                self.type_kitchen = ['итальянская', 'французская', 'украинская']
                for string in data:
                    self.database.append(self.__string_to_recipe__(string))
        except FileNotFoundError:
            print('Ошибка загрузки базы данных.')

    def recipes(self):
        return self.database

    @staticmethod
    def __string_to_recipe__(string):
        name = string.pop(0)
        author = string.pop(0)
        type_recipe = string.pop(0)
        description = string.pop(0)
        yt_link = string.pop(0)
        lst_ingred = string.pop(0)
        type_kitchen = string.pop(0)
        return Recipe(name, author, type_recipe, description, yt_link, lst_ingred, type_kitchen)

    @staticmethod
    def __recipe_to_string__(recipe):
        result = [recipe.name, recipe.author, recipe.type_recipe, recipe.description, recipe.yt_link,
                  recipe.lst_ingred, recipe.type_kitchen]
        return result

    def __save_data__(self):
        with open(self.filepath, 'w', encoding='utf-8', newline='') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__recipe_to_string__, self.database))

    def add_recipe(self, recipe_data):
        self.database.append(self.__string_to_recipe__(recipe_data))
        self.__save_data__()

    def get_recipes_by(self, name):
        names = list(map(str.strip, name.split(',')))
        recipes = []
        for name in names:
            for recipe in self.database:
                if name in ' '.join(map(str, recipe.__dict__.values())) and recipe not in recipes:
                    recipes.append(recipe)
        return recipes

    def remove_recipe(self, recipe):
        self.database.remove(recipe)
