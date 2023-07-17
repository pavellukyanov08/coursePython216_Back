from sqlalchemy import func

from models.customers import Customer
from models.sales import Sale
from models.salesmen import Salesman

from models.database import Session

from save_to_file_decorator import save_to_file

session = Session()


def key_query(table_name, ids):
    return session.get(table_name, ids)


def id_request(table_name, ids):
    return session.get(table_name, ids)


#@save_to_file
def get_records(table_name):
    return session.query(table_name)


#@save_to_file
def get_deal_by_salesman(salesman_id: int):
    return session.query(Sale.sales_id,
                         Sale.customer_id,
                         Sale.amt,
                         Salesman.sls_name).join(Salesman, Sale.salesman_id == Salesman.salesman_id)\
                                                .filter_by(salesman_id=salesman_id)


#@save_to_file
def max_sum_deal():
    return session.query(func.max(Sale.amt)).first()[0]


#@save_to_file
def min_sum_deal():
    return session.query(func.min(Sale.amt)).first()[0]


#@save_to_file
def max_sum_deal_by_specific_salesman(salesman_id: int):
    return session.query(func.max(Sale.amt), Salesman.sls_name)\
                    .join(Salesman, Sale.salesman_id == Salesman.salesman_id)\
                        .group_by(Salesman.sls_name).filter(Salesman.salesman_id == salesman_id)


#@save_to_file
def min_sum_deal_by_specific_salesman(salesman_id: int):
    return session.query(func.min(Sale.amt), Salesman.sls_name)\
                    .join(Salesman, Sale.salesman_id == Salesman.salesman_id)\
                        .group_by(Salesman.sls_name).filter(Salesman.salesman_id == salesman_id)


#@save_to_file
def max_sum_deal_by_specific_customer(customer_id: int):
    return session.query(func.max(Sale.amt), Customer.cust_name)\
                    .join(Customer, Sale.customer_id == Sale.customer_id)\
                        .group_by(Customer.cust_name).filter(Customer.customer_id == customer_id)


#@save_to_file
def min_sum_deal_by_specific_customer(customer_id: int):
    return session.query(func.min(Sale.amt), Customer.cust_name) \
        .join(Customer, Sale.customer_id == Sale.customer_id) \
        .group_by(Customer.cust_name).filter(Customer.customer_id == customer_id)


#@save_to_file
def max_sum_deal_by_all_salesman():
    return session.query(Sale.amt, Salesman.sls_name)\
                    .join(Sale, Sale.salesman_id == Salesman.salesman_id)\
                        .group_by(Sale.salesman_id) \
                            .order_by(func.sum(Sale.amt).desc())


#@save_to_file
def min_sum_deal_by_all_salesman():
    return session.query(Sale.amt, Salesman.sls_name)\
                    .join(Sale, Sale.salesman_id == Salesman.salesman_id)\
                        .group_by(Sale.salesman_id) \
                            .order_by(func.sum(Sale.amt))


#@save_to_file
def max_sum_deal_by_all_customer():
    return session.query(Customer.cust_name, func.sum(Sale.amt)) \
                    .join(Sale, Sale.customer_id == Customer.customer_id) \
                        .group_by(Sale.customer_id) \
                            .order_by(func.sum(Sale.amt).desc()) \


#@save_to_file
def avg_sum_sale_by_customer(salesman_id: int):
    return session.query(func.avg(Sale.amt), Salesman.sls_name)\
                        .join(Salesman, Sale.salesman_id == Salesman.salesman_id)\
                            .group_by(Salesman.sls_name)


#@save_to_file
def avg_sum_sale_by_seller(customer_id: int):
    return session.query(func.avg(Sale.amt), Customer.cust_name)\
                    .join(Customer, Sale.customer_id == Customer.customer_id)\
                        .group_by(Customer.cust_name)
