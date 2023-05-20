from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('recipe.csv')

    def run(self):
        command = None
        while command != '0':
            command = self.view.get_user_command()
            self.check_user_command(command)

    def check_user_command(self, command):
        if command == '1':
            recipe_data = self.view.get_recipe_data()
            self.model.add_recipe(recipe_data)

        elif command == '2':
            all_recipes = self.model.recipes()
            self.view.print_recipe(all_recipes)

        elif command == '3':
            target = self.view.find_recipe()
            recipes = self.model.get_recipes_by(target)
            self.view.print_recipe(recipes)

        elif command == '4':
            target = self.view.find_recipe()
            recipes = self.model.get_recipes_by(target)
            if len(recipes) > 1:
                number = self.view.remove_recipe(recipes)
                recipes = [recipes[number - 1]]
            self.model.remove_recipe(recipes[0])


