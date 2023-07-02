from abc import ABC, abstractmethod


class PizzaBase(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class PizzaBase25cm(PizzaBase):
    @property
    def get_cost(self):
        return 350

    def get_pizza(self):
        return f'Основа для пиццы 25 см'


class PizzaBase30cm(PizzaBase):
    @property
    def get_cost(self):
        return 500

    def get_pizza(self):
        return f'Основа для пиццы 30 см'


class PizzaTemplates(ABC):
    @abstractmethod
    def get_pizza(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class Toppings:
    data = {'Cheese': 15, 'Tomatoes': 15, 'Pepperoni': 20,
            'Bacon': 25, 'Mushrooms': 20, 'Olives': 25,
            'Chicken': 20, 'Pineapple': 20}

    def __init__(self, toppings=None):
        self.toppings = toppings
        self.toppings_cost = 0

    def get_toppings(self):
        if self.toppings is None:
            return 'Топинги отсутствуют'
        else:
            return ', '.join(topp for topp in self.toppings)

    def get_cost(self):
        if self.toppings is not None:
            for key, value in Toppings.data.items():
                for topp in self.toppings:
                    if key.lower() == topp.lower():
                        self.toppings_cost += value
        return self.toppings_cost


class MargaritaPizza(PizzaTemplates):
    def get_pizza(self, base=PizzaBase25cm()):
        return 'Маргарита: сыр, маринара, соус, баклажаны'

    def get_cost(self):
        return 350


class CarbonaraPizza(PizzaTemplates):
    def get_pizza(self, base=PizzaBase30cm()):
        return 'Карбонара: моцарелла, сын пармезан, яйца, бекон'

    def get_cost(self):
        return 430


class OwnPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Own pizza'

    def get_cost(self):
        return 600


class Pizza:
    def __init__(self, base, pizza, toppings):
        self.base = base
        self.pizza = pizza
        self.toppings = toppings

    @property
    def get_total_cost(self):
        return self.base.get_cost() + self.pizza.get_cost() + self.toppings.get_cost()


class PaymentMethod:
    def exec_transaction(self, amount):
        raise NotImplementedError


class CardPay(PaymentMethod):
    def exec_transaction(self, amount):
        return f'Заказ оплачен картой. Итоговая сумма: {amount} руб.'


class CashPay(PaymentMethod):
    def exec_transaction(self, amount):
        return f'Заказ оплачен наличными. Итоговая сумма: {amount} руб.'


class Payment:
    @staticmethod
    def do_payment(payment, amount):
        response = payment.exec_transaction(amount)
        print(response)


class Pizzeria:
    def __init__(self):
        self.sold_pizzas = 0
        self.revenue = 0
        self.profit = 0
        self.basket = []

    def run(self):
        command = None
        self.make_an_order()
        while command != '0':
            command = input('Введите команду:\n'
                            '1. Добавить пиццу в корзину\n'
                            '2. Удалить пиццу из корзины\n'
                            '3. Просмотреть ваш заказ\n'
                            '4. Очистить корзину\n'
                            '5. Оплатить товары в корзине:\n'
                            '6. Вывести данные о продажах\n'
                            '7. 0, чтобы выйти\n')

            if command == '1':
                self.add_pizza()

            elif command == '2':
                self.remove_pizza()

            elif command == '3':
                self.view_order()

            elif command == '4':
                self.clear_basket()

            elif command == '5':
                self.pay_card()

    def make_an_order(self):
        self.basket = []

    def add_pizza(self):
        command = input('Выберите опцию:\n'
                        '1. Выбрать одну из готовых пицц\n'
                        '2. Собрать пиццу самому!\n')

        if command == '1':
            pizza_templates = {'1': MargaritaPizza(), '2': CarbonaraPizza()}
            choice_pizza = input('Выберите пиццу: \n'
                                 '1: Маргарита\n'
                                 '2: Карбонара\n')

            size = input('Выберите размер (25 или 30 см): ')
            pizza_template = pizza_templates.get(choice_pizza)

            if pizza_template is None:
                print('Неверный ввод')

            if size == '25':
                pizza_base = PizzaBase25cm()

            elif size == '30':
                pizza_base = PizzaBase30cm()

            else:
                print('Ошибка ввода')
                return

            command_topping = input('Хотите добавить начинку? (y/n): ').strip().lower()
            if command_topping == 'y':
                toppings = input('Введите начинку через запятую: ').strip().split(',')
                pizza_toppings = Toppings(toppings)
            else:
                pizza_toppings = Toppings()
            pizza = Pizza(pizza_base, pizza_template, pizza_toppings)
            self.basket.append(pizza)
            print('Пицца добавлена в корзину.')

        elif command == '2':
            size = int(input('Выберите размер (25 или 30 см): '))
            if size == '25':
                pizza_base = PizzaBase25cm()

            elif size == '30':
                pizza_base = PizzaBase30cm()

            else:
                print('Ошибка ввода')
                return

            while True:
                topping_choice = input('Введите название топпинга (для завершения введите "Готово"): ')
                if topping_choice == 'Готово':
                    break
                else:
                    pizza_toppings = Toppings()
                    pizza = Pizza(pizza_base, OwnPizza(), pizza_toppings)
                    self.basket.append(pizza)
                    print('Пицца добавлена в корзину.')

    def remove_pizza(self):
        if len(self.basket) > 0:
            index = int(input('Введите номер пиццы для удаления: '))
            removed_pizza = self.basket.pop(index)
            print(f'Пицца "{removed_pizza}" удалена из корзины.')
        else:
            print('Корзина пуста.')

    def view_order(self):
        if len(self.basket) == 0:
            print('Корзина пуста.')

        else:
            print('Ваш заказ:')
            basket_info = ''
            for i, pizza in enumerate(self.basket, 1):
                basket_info += f'{i}. {pizza.base.get_pizza()} - {pizza.pizza.get_cost()} -> ' \
                               f'with {pizza.toppings.get_toppings()} for {pizza.get_total_cost} руб. \n'
            print(basket_info)
            return basket_info

    def save_cart(self):
        with open('file.txt', 'w') as f:
            data = self.view_order()
            if data == 'Корзина пуста.':
                return
            f.write(data)

    def clear_basket(self):
        if len(self.basket) > 0:
            self.basket = []
            print('Корзина очищена.')
        else:
            print('Корзина пуста.')

    def checkout(self):
        if not self.basket:
            print('Корзина пуста.')

        payment_method = input('Выберите способ оплаты: \n'
                               '1. Наличные'
                               '2. Карта')

        total_cost = sum(pizza.get_total_cost for pizza in self.basket)

        if payment_method == '1':
            Payment.do_payment(CashPay, total_cost)
            received_amount = float(input('Введите полученную сумму: '))

            if received_amount >= total_cost:
                change = received_amount - total_cost
                print(f'Спасибо за оплату! Сдача: {change} руб.')

        elif payment_method == '2':
            Payment.do_payment(CardPay, total_cost)
            print('Оплата произведена успешно.')

        self.sold_pizzas += len(self.basket)
        self.revenue += total_cost
        self.profit += total_cost - total_cost * 0.10
        self.make_an_order()


def main():
    app = Pizzeria()
    app.run()


if __name__ == '__main__':
    main()
