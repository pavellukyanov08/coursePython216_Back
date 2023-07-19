from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

us = env.get_template('products.html')

products = [
    {'name': 'Paper', 'price': 5},
    {'name': 'Paper', 'price': 10},
    {'name': 'Potato', 'price': 20},
    {'name': 'Cucumber', 'price': 30},
    {'name': 'Carrot', 'price': 40}
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
res = us.render(products=products)

print(res)
