from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model()
        except DecodeError as e:
            self.view.__throw_an_error__(e)

    def run(self):
        command = None
        while command != 'Выход':
            command = self.view.get_user_command()
            self.check_user_command(command)

    def check_user_command(self, command):
        if command == '1':
            shoes_data = self.view.add_new_shoe()
            self.model.add_new_shoe(shoes_data)
        # elif command == '2':
        #     all_shoes = self.model.shoes
        #     self.view.print_shoes(all_shoes)
        # elif command == '3':
        #     manuf = self.view.find_shoes()
        #     shoes = self.model.find_shoes(manuf)
        #     self.view.print_shoes(shoes)
        # elif command == '4':
        #     shoe_name = self.view.get_article_name()
        #     shoes = self.model.find_shoes([shoe_name])
        #     result = self.model.remove_shoes(shoes)
        #     if result == 'Слишком много статей':
        #         self.view.print_shoes(shoes)
        #         number = self.view.get_deletion_context()
        #         result = self.model.remove_shoes([shoes[number - 1]])
        #     self.view.return_delete_result(result)
        #
        #
