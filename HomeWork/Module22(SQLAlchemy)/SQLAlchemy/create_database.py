from faker import Faker

from models.database import create_db, Session

from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    customer_id = [2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009]
    cust_name = ['Hoffman', 'Giovanni', 'Liu', 'Grass', 'Clemens', 'Pereira', 'Cisneros', 'Karl']
    cust_city = ['London', 'Rome', 'San Jose', 'Berlin', 'London', 'Rome', 'San Jose', 'Rome']
    salesman_id = [1001, 1003, 1002, 1002, 1001, 1004, 1007, 1000]

    for i in range(len(customer_id)):
        customer = Customer(customer_id[i], cust_name[i], cust_city[i], salesman_id[i])
        session.add(customer)

    session.commit()

    sales_id = [3001, 3002, 3003, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012]
    salesman_id = [1007, 1004, 1001, 1002, 1007, 1002, 1001, 1003, 1002, 1001, 1000]
    customer_id = [2008, 2007, 2001, 2003, 2008, 2004, 2006, 2002, 2004, 2006, 2009]
    amt = [18.69, 767.19, 1900.1, 5160.45, 1098.16, 1713.23, 75.75, 4723, 1309.95, 9891.88, 421.3]
    sales_date = ['1990-03-10 00:00:00', '1990-03-10 00:00:00', '1990-03-10 00:00:00', '1990-03-10 00:00:00',
                  '1990-03-10 00:00:00', '1990-04-10 00:00:00', '1990-04-10 00:00:00', '1990-05-10 00:00:00',
                  '1990-06-10 00:00:00', '1990-06-10 00:00:00', '1990-06-10 00:00:00']

    for i in range(len(sales_id)):
        sales = Sale(sales_id[i], salesman_id[i], customer_id[i], amt[i], sales_date[i])
        session.add(sales)

    session.commit()

    salesman_id = [1000, 1001, 1002, 1003, 1004, 1007]
    sls_name = ['Rikki', 'Peel', 'Serres', 'Axelrod', 'Motika', 'Rifkin']
    sls_city = ['Rome', 'London', 'San Jose', 'New York', 'London', 'Barcelona']

    for i in range(len(salesman_id)):
        salesman = Salesman(salesman_id[i], sls_name[i], sls_city[i])
        session.add(salesman)

    session.commit()
    session.close()
