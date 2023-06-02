from jinja2 import Template

# person = {
#     'name': 'Иван',
#     'age': 26
# }
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}")
# msg = tm.render(p=person)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#
# person = Person('Иван', 26)
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.get_name() }}")
# msg = tm.render(p=person)
# print(msg)


# Фильтр {% raw %} при рендере не даёт шаблону вставить выражения
# data = """{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставит соответствующее значение {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name='Игорь')
# print(msg)


# Фильтр "| e" позволяет закодировать все специальные символы в код HTML
# link = """В HTML-документе ссылка определяется как
# <a href='#'>Ссылка</a>"""
#
# tm = Template("{{ link | e}}")
# msg = tm.render(link=link)
# print(msg)


# Работа с циклом for и условиями if elif else
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Смоленск'},
#     {'id': 4, 'city': 'Воронеж'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = """
# <select name='cities'>
# {% for c in cities -%}
# {% if c.id > 2 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% elif c.city == "Москва" -%}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)


# 1.
menu = [
    {'href': '/index', 'title': 'Главная'},
    {'href': '/news', 'title': 'О нас'},
    {'href': '/about', 'title': 'Новости'},
    {'href': '/shop', 'title': 'Магазин'},
    {'href': '/contacts', 'title': 'Контакты'}
]
text = """
<ul>
{% for m in menu -%}
{% if m['href'] == '/index' -%}
    <li><a href='{{ m['href'] }}' class='active'>{{ m['title'] }}</a><li>
{% else -%}
    <li><a href='{{ m['href'] }}'>{{ m['title'] }}</a><li>
{% endif -%}
{% endfor -%}
</ul>
"""
tm = Template(text)
msg = tm.render(menu=menu)
print(msg)


# Разнообразные фильтры для переменных
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17500},
#     {'model': 'Renault', 'price': 25000},
#     {'model': 'Wolksvagen', 'price': 20000}
# ]
# tpl = 'Суммарная цена автомобилей {{ cs | sum(attribute="price") }}'
# lst = [1, 2, 3, 4, 5]
# tm = Template('Суммарная цена автомобилей {{ cs | sum }}')
# tm = Template('Суммарная цена автомобилей {{ cs | max(attribute="price") }}')
# tm = Template('Суммарная цена автомобилей {{ (cs | min(attribute="price")).model }}')
# tm = Template('Суммарная цена автомобилей {{ cs | random }}')
# tm = Template('Суммарная цена автомобилей {{ cs | replace("model", "brand") }}')
# msg = tm.render(cs=cars)
# print(msg)


# Пример использования фильтров к большому количеству переменных
# persons = [
#     {"name": 'Алексей', 'year': 18, 'weight': 78.5},
#     {"name": 'Игорь', 'year': 20, 'weight': 82.2},
#     {"name": 'Иван', 'year': 25, 'weight': 87.1},
# ]
#
# tpl = """
# {%- for u in users -%}
#     {% filter upper -%} {{ u.name }} {% endfilter -%}
#     {% filter string -%} {{ u.year }} - {{ u.weight }} {% endfilter %}
# {% endfor -%}"""
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)


# Макроопределение
# html = '''
# {%- macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password') }}</p>
#
# '''
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# 2.
# html = """
# {%- macro input(name, placeholder, type='text') -%}
#     <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
# {%- endmacro %}
#
# <p>{{ input('firstname', 'Имя')}}</p>
# <p>{{ input('lastname', 'Фамилия')}}</p>
# <p>{{ input('address', 'Адрес')}}</p>
# <p>{{ input('phone', 'Телефон', 'tel')}}</p>
# <p>{{ input('email', 'Почта', 'email')}}</p>
# """
#
#
# tm = Template(html)
# msg = tm.render()
# print(msg)
