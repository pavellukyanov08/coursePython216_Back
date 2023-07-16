from jinja2 import Template

# person = {
#     'name': 'Иван',
#     'age': 20
# }
# tm = Template('Меня зовут {{ p.name }}. Мне {{ p.age }} лет')
# msg = tm.render(p=person)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def get_age(self):
#         return self.__age
#
#
# person = Person('Ivan', 20)
# tm = Template('Меня зовут {{ p.name }}. Мне {{ p.get_age }} лет')
# msg = tm.render(p=person)
# print(msg)

# data = '''Модуль Jinja вместе определения {{ name }} подставит соответствующее значение'''
# tm = Template(data)
# msg = tm.render(name='Egor')
# print(msg)


# link = '''В HTML-документе ссылка определяется так
#         <a href="#">Ссылка</a>'''
#
# tm = Template('{{ link | e }}')
# msg = tm.render(link=link)
# print(msg)

# cities = [
#     {'id': 1, 'name': 'Москва'},
#     {'id': 2, 'name': 'Сочи'},
#     {'id': 3, 'name': 'Казань'},
#     {'id': 4, 'name': 'Барнаул'}
# ]
#
# data = '''
# {% for city in cities -%}
#     {%- if city.id > 2 -%}
#         <p> {{ city.id, city.name }}</p>
#     {%- elif city.name == 'Москва' -%}
#         <h1> {{ cuty.name }}</h1>
#     {%- endif %}
# {% endfor %}
# '''
#
# tm = Template(data)
# msg = tm.render(cities=cities)
# print(msg)

# menu = [
#     {'url': '/index', 'name': 'Главная'},
#     {'url': '/news', 'name': 'Новости'},
#     {'url': '/about', 'name': 'О нас'},
#     {'url': '/shop', 'name': 'Магазин'},
#     {'url': '/contacts', 'name': 'Контакты'},
# ]
#
# tm = Template('''
# <ul>
# {% for el in menu -%}
#     {%- if el.url == 'index' %}
#     <li><a href="/{{ el.url}}" class="active">{{ el.name}}</a></li>
#     {%- else -%}
#     <li><a href="/{{ el.url}}">{{ el.name}}</a></li>
#     {%- endif %}
# {% endfor %}
# </ul>
# ''')
# msg = tm.render(menu=menu)
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 2000},
#     {'model': 'Skoda', 'price': 1900},
#     {'model': 'Renault', 'price': 1500},
#     {'model': 'Toyota', 'price': 2100}
# ]
#
# tm = Template('Результат фильтра {{ (cars | min(attribute="price")).model }}')
# msg = tm.render(cars=cars)
# print(msg)

# person = [
#     {'name': 'Виталий', 'year': 18, 'weight': 70},
#     {'name': 'Никита', 'year': 19, 'weight': 72.4},
#     {'name': 'Алексей', 'year': 21, 'weight': 76.1},
# ]

# tm = """
# {% for u in users -%}
#     {% filter title %}  {{ u.name }} человек {% endfilter %}
#     {% filter random %} {{ u.weight }} {% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tm)
# msg = tm.render(users=person)
# print(msg)

# html = """
# {% macro input(name, value='', type='text', size=20) %}
#     <input type="{{ type }} " name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# {% for name in ['username', 'email', 'password'] %}
#     <p> {{ input(name) }} </p>
# {% endfor %}
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# html = """
# {% macro input(name, placeholder, type='text') %}
#     <input type="{{ type }} " name="{{ name }}" placeholder="{{ placeholder }}">
# {% endmacro %}
#
# <p> {{ input('firstname', 'Имя')}} </p>
# <p> {{ input('lastname', 'Фамилия')}} </p>
# <p> {{ input('address', 'Адрес')}} </p>
# <p> {{ input('phone', 'Телефон', 'tel')}} </p>
# <p> {{ input('email', 'Почта', 'email')}} </p>
#
# """

# tm = Template(html)
# msg = tm.render()
# print(msg)


# person = [
#     {'name': 'Виталий', 'year': 18, 'weight': 70},
#     {'name': 'Никита', 'year': 19, 'weight': 72.4},
#     {'name': 'Алексей', 'year': 21, 'weight': 76.1},
# ]
#
# html = """
# {% macro list_users(users) %}
# <ul>
#     {% for u in users %}
#         <li>{{ u.name }}</li>
#     {% endfor %}
# </ul>
# {% endmacro %}
#
# {{ list_users(users) }}
# """
#
# tm = Template(html)
# msg = tm.render(users=person)
# print(msg)

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

tm = env.get_template('about.html')

subs = ['Культура', 'Наука', 'Спорт']

msg = tm.render(list_table=subs)
print(msg)
