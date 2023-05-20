import json


class Shoes:
    def __init__(self, type_shoes, gender, color, price, manufacturer, size):
        self.type_shoes = type_shoes
        self.gender = gender
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return f'{self.type_shoes} - {self.manufacturer}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self):
        self.filepath = 'shoes.txt'
        self.__shoes = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for shoe in self.data.values():
                self.__shoes[f'{shoe["type_shoes"]} {shoe["manufacturer"]}'] = Shoes(*shoe.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = {shoe.type_shoes: shoe.__dict__ for shoe in self.__shoes.values()}
        json.dump(dict_shoes, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_shoe(self, shoe_data):
        new_shoe = Shoes(*shoe_data.values())
        self.__shoes[f'{new_shoe.type_shoes} {new_shoe.manufacturer} {new_shoe.gender}'] = new_shoe
        self.save_shoes()

    def find_shoes(self, criteria):
        shoes = []
        for shoe in self.__shoes.values():
            for crit in criteria:
                if shoe in shoes:
                    break
                for spec in shoe.__dict__.values():
                    if crit.lower() in spec.lower():
                        shoes.append(shoe)
                        break
        return shoes

    def remove_shoes(self, shoes):
        if len(shoes) == 0:
            return 'Обувь не найдена'
        elif len(shoes) == 1:
            shoe = shoes[0]
            key = f'{shoe.type_shoes} {shoe.manufacturer}'
            self.__shoes.pop(key)
            self.save_shoes()
            return 'Обувь удалена'
        else:
            return 'Пар обуви слишком много'
