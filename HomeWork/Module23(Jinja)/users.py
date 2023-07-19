from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

us = env.get_template('users.html')

users = [
    {'name': 'Sam', 'email': 'sam@mail.ru'},
    {'name': 'John', 'email': 'john@yandex.ru'},
    {'name': 'Michael', 'email': 'michael@gmail.com'},
    {'name': 'Adam', 'email': 'adam@gmail.com'}
]

# user = '''
#     {%- macro list_users(users) -%}
#         {%- for user in users -%}
#             {%- if user.email.endswith('@gmail.com') %}
#                 <p>{{ user.name }} -> {{ user.email }}</p>
#             {%- endif -%}
#         {%- endfor -%}
#     {%- endmacro -%}
#
#     {{ list_users(users) }}
# '''

# us = Template(user)
res = us.render(users=users)
print(res)
