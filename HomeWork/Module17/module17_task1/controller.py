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
            command = self.view.wait_user_answer()
            self.check_user_answer(command)

    def check_user_answer(self, command):
        if command == '1':
            shoe_data = self.view.add_new_shoe()
            self.model.add_new_shoe(shoe_data)
        elif command == '2':
            all_shoes = self.model.shoes
            self.view.print_shoes(all_shoes)
        elif command == '3':
            manuf = self.view.find_shoes()
            shoes = self.model.find_shoes(manuf)
            self.view.print_shoes(shoes)
        elif command == '4':
            # choice = input('Выберите способ удаления: (n - по номеру, m - производителю')
            # if choice == 'n':
            #     number = self.view.remove_by_num()
            #     shoe_num = self.model.find_shoes(number)
            #     remove_num_result = self.model.remove_shoes(shoe_num)
            #     self.view.return_delete_result(remove_num_result)
            # else:
            # manuf = self.view.remove_by_manuf()
            # shoe_manuf = self.model.find_shoes(manuf)
            # remove_manuf_result = self.model.remove_shoes(shoe_manuf)

            shoe_manuf = self.view.remove_by_manuf()
            shoes = self.model.find_shoes([shoe_manuf])
            result = self.model.remove_shoes(shoes)
            if result == 'Пар обуви слишком много':
                self.view.print_shoes(shoes)
                number = self.view.remove_by_num()
                result = self.model.remove_shoes([shoes[number - 1]])
            self.view.return_delete_result(result)
