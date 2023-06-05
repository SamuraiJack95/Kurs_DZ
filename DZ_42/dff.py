import re
users= [{'name': 'andrey', 'email': 'andrey@gmail.com'},
       {'name': 'sergey', 'email': 'sergey@gmail.com'},
       {'name': 'ivan', 'email': 'ivan@mail.com'},
       {'name': 'pety', 'email': 'pety@mail.com'},
       {'name': 'artem', 'email': 'artem@mail.com'}]

# for u in range(len(users)):
#     tuy = users[u]['email'].split('@')
#     if tuy == 'gmail.com':
#         print(users[u]['email'])

# for u in range(len(users)):
#     b = users[u]['email']
#     if re.search('gmail.com', b):
#         print(users[u]['email'])

for u in users:
    b = u['email']
    if re.search('gmail.com', b):
        print(u['email'])
