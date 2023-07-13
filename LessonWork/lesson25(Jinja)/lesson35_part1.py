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

menu = [
    {'url': '/index', 'name': 'Главная'},
    {'url': '/news', 'name': 'Новости'},
    {'url': '/about', 'name': 'О нас'},
    {'url': '/shop', 'name': 'Магазин'},
    {'url': '/contacts', 'name': 'Контакты'},
]

tm = Template('''
<ul>
{% for el in menu -%}
    {%- if el.url == 'index' %}
    <li><a href="/{{ el.url}}" class="active">{{ el.name}}</a></li>
    {%- else -%}
    <li><a href="/{{ el.url}}">{{ el.name}}</a></li>
    {%- endif %}
{% endfor %}
</ul>
''')
msg = tm.render(menu=menu)
print(msg)
