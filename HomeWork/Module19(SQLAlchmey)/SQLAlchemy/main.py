import os

from sqlalchemy import and_, not_, or_, func
from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer

from models.database import DATABASE_NAME, Session
import create_database as db_creator


class UserMenu:
    session = Session()

    while True:
        choice_action = input('Выберите действие (1 - выборка, 2 - вставка, 3 - обновление, 4 - удаление): ')
        if choice_action == '1':
            command = input('Введите команду: ')

            if command == '1':
                # Все сделки
                for i, elem in enumerate(session.query(Sale), 1):
                    print(f'{i}. {elem}')

            elif command == '2':
                # Сделки конкретного продавца
                for i, salesman in enumerate(session.query(Salesman), 1):
                    print(f'{i}. {salesman}')
                print()

                seller_name = input('Введите имя: ')
                if seller_name in session.query(Sale).join(Salesman).filter_by(sls_name=seller_name):
                    print(seller_name)
                else:
                    print('Продавец не найден')
                print('===' * 20)

            elif command == '3':
                # Макс. сумма сделки
                for deal in session.query(func.max(Sale.amt)):
                    print(*deal)
                # max_deal = session.query(func.max(Sale.amt))
                # print(max_deal.first()[0])

            elif command == '4':
                # Мин. сумма сделки
                for deal in session.query(func.min(Sale.amt)):
                    print(*deal)

            elif command == '5':
                # Макс. сумма сделки для каждого продавца
                for i, deal in enumerate(session.query(func.max(Sale.amt), Salesman.sls_name).join(Salesman).group_by(
                        Salesman.sls_name), 1):
                    print(f'{i}. {deal}')

            elif command == '6':
                # Мин. сумма сделки для каждого продавца
                for i, deal in enumerate(session.query(func.min(Sale.amt), Salesman.sls_name).join(Salesman).group_by(
                        Salesman.sls_name), 1):
                    print(f'{i}. {deal}')

            elif command == '7':
                # Макс. сумма сделки для каждого покупателя
                for i, deal in enumerate(session.query(func.max(Sale.amt), Customer.cust_name).join(Customer).group_by(
                        Customer.cust_name), 1):
                    print(f'{i}. {deal}')

            elif command == '8':
                # Мин. сумма сделки для каждого покупателя
                for i, deal in enumerate(session.query(func.min(Sale.amt), Customer.cust_name).join(Customer).group_by(
                        Customer.cust_name), 1):
                    print(f'{i}. {deal}')

            elif command == '9':
                # Макс. по сумме сделка для каждого продавца. ДОДЕЛАТЬ!!!
                for i, deal in enumerate(session.query(func.sum(Sale.amt), Salesman.sls_name).join(Salesman).group_by(
                        Salesman.sls_name), 1):
                    print(f'{i}. {deal}')

            elif command == '10':
                # Мин. по сумме сделка для каждого продавца. ДОДЕЛАТЬ!!!
                for i, deal in enumerate(session.query(func.sum(Sale.amt), Salesman.sls_name).join(
                        Salesman).group_by(Salesman.sls_name).order_by(Salesman.amt.desc()), 1):
                    print(f'{i}. {deal}')

            elif command == '11':
                # Макс. сумма покупок покупателя.
                for i, deal in enumerate(session.query(func.max(Sale.amt), Customer.cust_name).join(Customer), 1):
                    print(f'{i}. {deal}')

            elif command == '12':
                # Мин. сумма покупок покупателя.
                for i, deal in enumerate(session.query(func.min(Sale.amt), Customer.cust_name).join(Customer), 1):
                    print(f'{i}. {deal}')

            elif command == '13':
                # Ср. сумма покупок для каждого покупателя.
                for i, deal in enumerate(session.query(func.avg(Sale.amt), Customer.cust_name).join(Customer).group_by(
                        Customer.cust_name), 1):
                    print(f'{i}. {deal}')

            elif command == '14':
                # Ср. сумма покупок для каждого продавца.
                for i, deal in enumerate(session.query(func.avg(Sale.amt), Salesman.sls_name).join(Salesman).group_by(
                        Salesman.sls_name), 1):
                    print(f'{i}. {deal}')

        elif choice_action == '2':
            print('Меню вставки данных \n')

            choice_table = input('Выберите таблицу (1 - customers, 2 - sales, 3 - salesmen): ')
            if choice_table == '1':
                new_cust_id = int(input('Введите id покупателя: '))
                new_cust_name = input('Введите имя покупателя: ')
                new_cust_city = input('Введите город покупателя: ')
                new_salesman_id = int(input('Введите id продавца: '))

                customer = Customer(new_cust_id, new_cust_name, new_cust_city, new_salesman_id)
                session.add(customer)

                session.commit()

            elif choice_table == '2':
                new_sales_id = int(input('Введите id товара: '))
                new_salesman_id = int(input('Введите id продавца: '))
                new_customer_id = int(input('Введите id покупателя: '))
                new_amt = int(input('Введите сумму товара: '))
                new_sales_date = input('Введите дату сделки: ')

                sale = Sale(new_sales_id, new_salesman_id, new_customer_id, new_amt, new_sales_date)
                session.add(sale)

                session.commit()

            elif choice_table == '3':
                new_salesman_id = int(input('Введите id продавца: '))
                new_sls_name = input('Введите имя продавца: ')
                new_sls_city = input('Введите город продавца: ')

                salesman = Salesman(new_salesman_id, new_sls_name, new_sls_city)
                session.add(salesman)

                session.commit()

        elif choice_action == '3':
            print('Меню обновления данных \n')

            choice_table = input('Выберите таблицу (1 - customers, 2 - sales, 3 - salesmen): ')

            if choice_table == '1':
                for i, cust in enumerate(session.query(Customer), 1):
                    print(f'{i}. {cust}')

                id = input("Введите ID покупателя, которого хотите обновить: ")
                if id in session.query(Customer):
                    record = session.query(Customer).filter_by(id=id).one()
                else:
                    print("Запись с указанным ID не найдена.")

                new_cust_id = int(input('Введите id покупателя: '))
                new_cust_name = input('Введите имя покупателя: ')
                new_cust_city = input('Введите город покупателя: ')
                new_salesman_id = int(input('Введите id продавца: '))

                # Обновляем значения атрибутов объекта
                record.new_cust_id = new_cust_id
                session.commit()

                print("Данные успешно обновлены!")

                salesman = Salesman(new_salesman_id, new_sls_name, new_sls_city)
                session.add(salesman)

                session.commit()


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
    UserMenu()
