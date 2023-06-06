from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

product = [{'name': 'картошка', 'Price': 8},
       {'name': 'помидор', 'Price': 12},
       {'name': 'стиральный порошок', 'Price': 18},
       {'name': 'утюг', 'Price': 25},
       {'name': 'хлопья', 'Price': 6}]

tm = env.get_template('main.html')
msg = tm.render(users=product)
print(msg)