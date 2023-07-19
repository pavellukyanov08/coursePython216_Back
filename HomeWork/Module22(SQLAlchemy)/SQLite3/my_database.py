import sqlite3 as sq

# В дз использовано 2 базы: 'clinic' (создание таблиц, запросы на вставку, обновление, изменение удаление данных и
# изменение структуры самой таблицы) и 'shop' (база с прошлых дз, взята под запросы с использованием связей)

# with sq.connect('clinic.db') as conn:
with sq.connect('shop.db') as conn:
    cur = conn.cursor()

    # Запросы на создание таблицы

    # cur.execute('''CREATE TABLE IF NOT EXISTS clients(
    #                 client_id INTEGER PRIMARY KEY,
    #                 name text,
    #                 age integer,
    #                 birthday text,
    #                 address text
    #                 )''')

    # cur.execute('''CREATE TABLE IF NOT EXISTS doctors(
    #                 doctor_id INTEGER PRIMARY KEY,
    #                 name text,
    #                 age integer,
    #                 birthday text,
    #                 address text
    #                 )''')

    # cur.execute('''CREATE TABLE registrator (
    #                 staff_id INTEGER PRIMARY KEY,
    #                 name TEXT NOT NULL,
    #                 age INTEGER,
    #                 address TEXT
    #                 );''')

    # Запросы на вставку
    # clients = [
    #     (2, 'Michael', 20, 'Попова 98'),
    #     (3, 'John', 18, 'Песчаная 102'),
    #     (4, 'Peter', 25, 'Смирнова 80'),
    # ]

    # cur.executemany('''insert into clients values(?, ?, ?, ?)''', clients)
    # cur.executescript('''insert into clients values(5, 'Nikolay', 30, 'Пушкина 7');
    #                     insert into clients values(6, 'Semen', 46, 'Алеексеева 90');
    #                     insert into clients values(7, 'Andrey', 50, 'Социалистический 10')''')

    # doctors = [
    #     (1, 'Semen', 35, 'Ленина 97', 'Ортопед'),
    #     (2, 'Pavel', 29, 'Малахова 101','Хирург'),
    #     (3, 'Dmitriy', 40, 'Димитрова 50', 'Дантист'),
    #     (4, 'Alexey', 32, 'А. Петрона 21', 'Ортодонт'),
    # ]
    # cur.executemany('''insert into doctors values(?, ?, ?, ?, ?)''', doctors)

    # cur.executemany('''insert into clients values(?, ?, ?, ?)''', clients)
    # cur.execute('''insert into registrator values(3, 'Natalia', 24, 'Социалистический 90')''')

    # Изменения таблиц
    # cur.execute('''alter table doctors
    #                 add column spec text''')

    # cur.execute('''alter table staff
    #                 rename to registrator''')

    # cur.execute('''alter table registrator
    #                 drop column post''')

    # with open('clients.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         client_id, name, age, address = line.strip().split(',')
    #
    #         cur.execute('''insert into clients values(?, ?, ?, ?)''', (client_id, name, age, address))

    # Взял нашу базу, которая была с дз, переименовал в 'shop'
    # cur.execute('''select cname, c.city, sp.sname, sp.city
    #                 from customers c
    #                 join salespeople sp on c.snum = sp.snum
    #                 where c.city = sp.city''')

    # cur.execute('''select cname, avg(amt)
                        # from customers c, orders o
                        # where amt < (select avg(amt) from orders)
                        # group by cname''')

    # cur.execute('''select cname, sname, com
    #                 from customers c, salespeople sp
    #                 where c.snum = sp.snum
    #                 group by cname''')

    rows = cur.fetchall()

    for row in rows:
        print(row)

