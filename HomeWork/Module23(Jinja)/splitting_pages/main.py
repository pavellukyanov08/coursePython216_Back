from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

prod = env.get_template('index.html')

users = [
    {'name': 'Sam', 'email': 'sam@mail.ru'},
    {'name': 'John', 'email': 'john@yandex.ru'},
    {'name': 'Michael', 'email': 'michael@gmail.com'},
    {'name': 'Adam', 'email': 'adam@gmail.com'}
]

# prod = Template(product)
res = prod.render(users=users)

print(res)
