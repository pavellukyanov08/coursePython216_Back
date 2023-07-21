from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

prod = env.get_template('users_and_products.html')

products = [
    {'name': 'Paper', 'price': 5},
    {'name': 'Paper', 'price': 10},
    {'name': 'Potato', 'price': 20},
    {'name': 'Cucumber', 'price': 30},
    {'name': 'Carrot', 'price': 40}
]

users = [
    {'name': 'Sam', 'email': 'sam@mail.ru'},
    {'name': 'John', 'email': 'john@yandex.ru'},
    {'name': 'Michael', 'email': 'michael@gmail.com'},
    {'name': 'Adam', 'email': 'adam@gmail.com'}
]

# product = '''
#     {% macro product_list(products) %}
#         <ul>
#             {%- for prod in products -%}
#                 {%- if prod.price < 10 %}
#                 <li> {{ prod.name }} : {{ prod.price }} -> доступный
#
#                 {%- elif prod.price <= 20 %}
#                 <li> {{ prod.name }} : {{ prod.price }} -> средняя цена
#
#                 {%- elif prod.price <= 30 %}
#                 <li> {{ prod.name }} : {{ prod.price }} -> цена выше средней
#
#                 {%- else %}
#                 <li> {{ prod.name }} : {{ prod.price }} -> дорогой
#
#                 {%- endif %}
#             {%- endfor %}
#         </ul>
#     {% endmacro -%}
#
#     {{product_list(products)}}
#
# '''

# prod = Template(product)
res = prod.render(products=products, users=users)

print(res)
