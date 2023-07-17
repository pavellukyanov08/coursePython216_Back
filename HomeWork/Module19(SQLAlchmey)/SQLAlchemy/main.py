import os

from query_func import \
    key_query, \
    id_request, \
    get_records, \
    get_deal_by_salesman, \
    max_sum_deal, \
    min_sum_deal, \
    max_sum_deal_by_specific_salesman, \
    min_sum_deal_by_specific_salesman, \
    max_sum_deal_by_specific_customer, \
    min_sum_deal_by_specific_customer, \
    max_sum_deal_by_all_salesman, \
    min_sum_deal_by_all_salesman, \
    max_sum_deal_by_all_customer, \
    avg_sum_sale_by_customer, \
    avg_sum_sale_by_seller

from sqlalchemy import func

from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from save_to_file_decorator import save_to_file

session = Session()


def user_menu():
    while True:
        choice_action = input('Выберите действие (1 - выборка, 2 - вставка, 3 - обновление, 4 - удаление): ')
        if choice_action == '1':
            command = input('Введите команду: ')

            if command == '1':
                # Все сделки
                all_deal = [print(f'{i}. {deal}') for i, deal in enumerate(get_records(Sale), 1)]

            elif command == '2':
                # Сделки конкретного продавца
                all_seller = [print(f'{i}. {seller}') for i, seller in enumerate(get_records(Salesman), 1)]
                print()

                user_query = get_deal_by_salesman(int(input('Введите ID: ')))
                if user_query:
                    for row in user_query:
                        print(row)
                else:
                    print('Продавец не найден')

                print('===' * 20)

            elif command == '3':
                # Макс. сумма сделки
                print(max_sum_deal())

            elif command == '4':
                # Мин. сумма сделки
                print(min_sum_deal())

            elif command == '5':
                # Макс. сумма сделки для конкретного продавца
                all_seller = [print(f'{i}. {seller}') for i, seller in enumerate(get_records(Salesman), 1)]

                user_query = max_sum_deal_by_specific_salesman(int(input('Введите ID продавца: ')))

                if user_query:
                    for row in user_query:
                        print(row)
                else:
                    print('Продавец не найден')

            elif command == '6':
                # Мин. сумма сделки для конкретного продавца
                all_seller = [print(f'{i}. {seller}') for i, seller in enumerate(get_records(Salesman), 1)]

                user_query = min_sum_deal_by_specific_salesman(int(input('Введите ID продавца: ')))

                if user_query:
                    for row in user_query:
                        print(row)
                else:
                    print('Продавец не найден')

            elif command == '7':
                # Макс. сумма сделки для конкретного покупателя
                all_customers = [print(f'{i}. {cust}') for i, cust in enumerate(get_records(Customer), 1)]

                user_query = max_sum_deal_by_specific_customer(int(input('Введите ID покупателя: ')))

                if user_query:
                    for row in user_query:
                        print(row)
                else:
                    print('Покупатель не найден')

            elif command == '8':
                # Мин. сумма сделки для конкретного покупателя
                all_customers = [print(f'{i}. {cust}') for i, cust in enumerate(get_records(Customer), 1)]

                user_query = min_sum_deal_by_specific_customer(int(input('Введите ID покупателя: ')))

                if user_query:
                    for row in user_query:
                        print(row)
                else:
                    print('Покупатель не найден')

            elif command == '9':
                # Продавец, у которого макс. сумма продаж по всем сделкам
                user_query = [print(f'{i}. {seller}') for i, seller in enumerate(max_sum_deal_by_all_salesman(), 1)]

            elif command == '10':
                # Продавец, у которого мин. сумма продаж по всем сделкам
                user_query = [print(f'{i}. {seller}') for i, seller in enumerate(min_sum_deal_by_all_salesman(), 1)]

            elif command == '11':
                # Покупателя, у которого макс. сумма покупок по всем сделкам
                user_query = [print(f'{i}. {cust}') for i, cust in enumerate(max_sum_deal_by_all_customer(), 1)]

            elif command == '12':
                # Ср. сумма покупок для каждого покупателя.
                user_query = [print(f'{i}. {cust}') for i, cust in enumerate(avg_sum_sale_by_customer(int(input(
                                                                                    'Введите ID покупателя: '))), 1)]

            elif command == '13':
                # Ср. сумма покупок для каждого продавца.
                user_query = [print(f'{i}. {seller}') for i, seller in enumerate(avg_sum_sale_by_seller(int(input(
                    'Введите ID покупателя: '))), 1)]

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
                user_request = [print(f'{i}. {cust}') for i, cust in enumerate(session.query(Customer), 1)]

                cust_id = int(input("Введите ID покупателя, которого хотите обновить: "))
                key_request = id_request(Customer, cust_id)

                if key_request:
                    new_cust_id = int(input('Введите новый id покупателя: '))
                    new_cust_name = input('Введите новое имя покупателя: ')
                    new_cust_city = input('Введите новый город покупателя: ')
                    new_salesman_id = int(input('Введите новый id продавца: '))
                    query = session.get(Customer, cust_id)
                    update_query = session.query(Customer).filter_by(customer_id=cust_id)
                    data_update = dict(customer_id=new_cust_id,
                                       cust_name=new_cust_name,
                                       cust_city=new_cust_city,
                                       salesman_id=new_salesman_id)
                    update_query.update(data_update)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")

            if choice_table == '2':
                user_request = [print(f'{i}. {sale}') for i, sale in enumerate(session.query(Sale), 1)]

                sale_id = int(input("Введите ID товара, которого хотите обновить: "))
                key_request = id_request(Sale, sale_id)

                if key_request:
                    new_sales_id = int(input('Введите новый id товара: '))
                    new_slsman_id = int(input('Введите новый id продавца: '))
                    new_cust_id = int(input('Введите новый id покупателя: '))
                    new_amt = float(input('Введите новую цену товара: '))
                    query = session.get(Sale, sale_id)
                    update_query = session.query(Sale).filter_by(sales_id=sale_id)
                    data_update = dict(sales_id=new_sales_id,
                                       salesman_id=new_slsman_id,
                                       customer_id=new_cust_id,
                                       amt=new_amt)
                    update_query.update(data_update)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")

            if choice_table == '3':
                user_request = [print(f'{i}. {seller}') for i, seller in enumerate(session.query(Salesman), 1)]

                seller_id = int(input("Введите ID продавца, которого хотите обновить: "))
                key_request = id_request(Salesman, seller_id)

                if key_request:
                    new_salesman_id = int(input('Введите новый id продавца: '))
                    new_sls_name = input('Введите новое имя продавца: ')
                    new_sls_city = input('Введите новый город продавца: ')
                    query = session.get(Salesman, seller_id)
                    update_query = session.query(Salesman).filter_by(salesman_id=seller_id)
                    data_update = dict(salesman_id=new_salesman_id,
                                       sls_name=new_sls_name,
                                       sls_city=new_sls_city)
                    update_query.update(data_update)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")

        elif choice_action == '4':
            print('Меню удаления данных \n')

            choice_table = input('Выберите таблицу (1 - customers, 2 - sales, 3 - salesmen): ')
            if choice_table == '1':
                user_request = [print(f'{i}. {cust}') for i, cust in enumerate(session.query(Customer), 1)]

                cust_id = input("Введите ID покупателя, который хотите удалить: ")
                record = id_request(Customer, cust_id)

                if record:
                    session.delete(record)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")

            if choice_table == '2':
                user_request = [print(f'{i}. {sale}') for i, sale in enumerate(session.query(Sale), 1)]

                sales_id = int(input("Введите ID товара, который хотите удалить: "))

                record = id_request(Sale, sales_id)
                if record:
                    session.delete(record)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")

            if choice_table == '3':
                user_request = [print(f'{i}. {seller}') for i, seller in enumerate(session.query(Salesman), 1)]

                seller_id = input("Введите ID продавца, который хотите удалить: ")
                record = id_request(Salesman, seller_id)

                if record:
                    session.delete(record)
                    session.commit()
                else:
                    print("Запись с указанным ID не найдена.")


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    user_menu()
