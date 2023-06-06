# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         cls.__init__(cls._instance, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self):
#         pass
#
#
# class DatabaseConnection(Singleton):
#     def __init__(self, x):
#         super().__init__()
#         self.x = x
#
#
# a=3
# dbc1 = DatabaseConnection(a)
# print(dbc1)
# dbc2 = DatabaseConnection(a)
# print(dbc2)
#
# print(dbc1.x)


# class Wheel:
#     def __str__(self):
#         return 'wheel 21'
#
#
# class Engine:
#     def __str__(self):
#         return 'engine 4.4l'
#
#
# class Body:
#     def __str__(self):
#         return 'sedan'
#
#
# class Car:
#     def __init__(self):
#         pass
#
#
# class CarBuilder:
#     def __init__(self):
#         self.car = Car()
#
#     def get_wheel(self):
#         return Wheel()
#
#     def get_engine(self):
#         return Engine()
#
#     def get_body(self):
#         return Body()
#
#     def get_car(self):
#         return self.car
#
#     def build_car(self):
#         self.car.wheel = self.get_wheel()
#         self.car.engine = self.get_engine()
#         self.car.body = self.get_body()
#
#
# builder = CarBuilder()
# builder.build_car()
# car1 = builder.get_car()
#
# print(car1.__dict__.keys())


class CreditCardStrategy:
    @staticmethod
    def pay():
        print('Оплата картой прошла успешно ')


class PayPalStrategy:
    @staticmethod
    def pay():
        print('Оплата через PayPal прошла успешно')


class PaymentProcessor:
    def __init__(self, strategy=CreditCardStrategy()):
        self.strategy = strategy

    def get_payment(self):
        self.strategy.pay()

    def switch_strategy(self):
        choice = input('Введите вид оплаты: 1) карта, 2) paypal')
        choose_payment = {'1': CreditCardStrategy, '2': PayPalStrategy}
        if choice in choose_payment:
            self.strategy = choose_payment[choice]()
        else:
            print('Данного варианта оплаты не существует')


payment = PaymentProcessor()
payment.get_payment()
payment.switch_strategy()
payment.get_payment()


