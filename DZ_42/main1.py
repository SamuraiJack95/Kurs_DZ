from jinja2 import Template
import re

users= [{'name': 'andrey', 'email': 'andrey@gmail.com'},
       {'name': 'sergey', 'email': 'sergey@gmail.com'},
       {'name': 'ivan', 'email': 'ivan@mail.com'},
       {'name': 'pety', 'email': 'pety@mail.com'},
       {'name': 'artem', 'email': 'artem@mail.com'}]


html = """
{%- macro printt(name, email) -%}
    <print 'name: ' {{ name }} 'email: ' {{ email }}>
{%- endmacro -%}

<p>
{%- for u in range(len(users)) -%}
    {{ b = users[u]['email'] }}
    {% if re.search('gmail.com', b) %}
            {% printt({{u['name']}}, {{u['email']}} %}
    {% endif -%}  
{% endfor -%}
<p>
"""


tm = Template(html)
msg = tm.render(users=users)
print(msg)
