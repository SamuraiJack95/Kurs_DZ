from jinja2 import Template
import re

# ZD_1
users= [{'name': 'andrey', 'email': 'andrey@gmail.com'},
       {'name': 'sergey', 'email': 'sergey@gmail.com'},
       {'name': 'ivan', 'email': 'ivan@mail.com'},
       {'name': 'pety', 'email': 'pety@mail.com'},
       {'name': 'artem', 'email': 'artem@mail.com'}]


html = """
{%- macro printt(users) -%}
<p>
{% for u in users -%}
    {% if re.search('gmail.com', u['email']) -%}
        <p>{{u['name']}} - {{u['email']}}</p>
    {%- endif %}
{% endfor -%}
</p>
{% endmacro%}

{{printt(users)}}

"""

tm = Template(html)
msg = tm.render(users=users, re=re)
print(msg)

# ZD_2

# product = [{'name': 'картошка', 'Price': 8},
#        {'name': 'помидор', 'Price': 12},
#        {'name': 'стиральный порошок', 'Price': 18},
#        {'name': 'утюг', 'Price': 25},
#        {'name': 'хлопья', 'Price': 6}]
#
#
# html = """
# {% macro price(product) -%}
# <ul>
# {%- for u in product -%}
#     {%- if u['Price'] < 10 %}
#         <li> {{u['name']}} - {{u['Price']}} - низкая цена </li>
#     {%- elif u['Price'] < 20 %}
#         <li> {{u['name']}} - {{u['Price']}} - средняя цена </li>
#     {%- elif u['Price'] > 20 %}
#         <li> {{u['name']}} - {{u['Price']}} - высокая цена </li>
#     {%- endif %}
# {%- endfor %}
# </ul>
# {%- endmacro-%}
#
# {{price(product)}}
#
# """
#
# tm = Template(html)
# msg = tm.render(product=product, re=re)
# print(msg)
