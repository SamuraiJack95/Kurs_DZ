from jinja2 import Template
import re

users= [{'name': 'andrey', 'email': 'andrey@gmail.com'},
       {'name': 'sergey', 'email': 'sergey@gmail.com'},
       {'name': 'ivan', 'email': 'ivan@mail.com'},
       {'name': 'pety', 'email': 'pety@mail.com'},
       {'name': 'artem', 'email': 'artem@mail.com'}]


html = """
{% macro printt(users) %}
<p>
{% for u in users %}
     b = {{ u['email'] }}
    {% if re.search('gmail.com', b) %}
        <p>{{u['name']}} {{u['email']}}</p> 
    {% endif %}  
{% endfor %}
</p>
{% endmacro %}

{{printt(users)}}

"""



tm = Template(html)
msg = tm.render(users=users, re=re)
print(msg)
