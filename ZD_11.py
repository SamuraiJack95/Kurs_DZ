# ZD_1

ballsports = {'Качитков Михаил Евгенивевич': '189', 'Хорошейкин Иван Петровович': '186', 'Долгополов Михаил Васильевич': '191'}

command = input('Введите команду: add/replace/delete/find/exit')

while command != 'exit':
    if command == 'add' or command == 'replace':
        fio = input('Введите ФИО спортсмена которого хотите добавить')
        data = input('Введите рост')
        ballsports[fio] = data
        if command == 'replace':
            print('данные были изменены')
        else:
            print('данные добавлены')

    elif command == 'del':
        fio = input('Введите ФИО сотрудника у которого хотите что - то удалить')
        del ballsports[fio]
        print('данные были удалены')

    elif command == 'find':
        fio = input('Введите ФИО сотрудника у которого хотите найти')
        data = ballsports.get(fio)
        print(data)

    elif command == 'exit':
        break
    command = input('Введите команду: add/replace/delete/find/exit')

print(ballsports)
# ZD_3


# workers = {'Долгополов Михаил Васильевич':
#          {'телефон':'+79276789045', 'почта':'rupldan@gmail.com', 'должность': 'клерк', 'skype': 'aergont', 'кабинет': '26'},
#
#          'Прокопинкина Мария Владиславовна':
#          {'телефон': '+79274566045', 'почта': 'markon@gmail.com', 'должность': 'начальник', 'skype': 'limbortn', 'кабинет': '15'},
#
#          'Хорошейкин Иван Петровович':
#          {'телефон': '+79276074687', 'почта': 'megadan@gmail.com', 'должность': 'менеджер', 'skype': 'akolt', 'кабинет': '5'}}
#
# print(workers)
#
# print(workers['Долгополов Михаил Васильевич'])
#
# command = input('Введите команду: add/add data/replace/delete/find/exit')
#
# while command != 'exit':
#     if command == 'add':
#         fio = input('Введите ФИО сотрудника которого хотите добавить')
#         workers[fio] = {}
#         check = input('что хотите поменять или добавить?')
#         data = input('Введите данные')
#         workers[fio][check] = data
#         print('данные были добавлены')
#
#     elif command == 'add data' or command == 'replace':
#         fio = input('Введите ФИО сотрудника у которого хотите что - то поменять')
#         check = input('что хотите поменять или добавить?')
#         data = input('Введите данные')
#         workers[fio][check] = data
#         print('данные были изменены')
#         if command == 'add data':
#             print('данные добавлены')
#     elif command == 'del':
#         fio = input('Введите ФИО сотрудника у которого хотите что - то удалить')
#         chekk = input('1.удалить полностью, 2. удалить выбранные данные')
#         if chekk == '1':
#             del workers[fio]
#             print('данные были удалены')
#         elif chekk == '2':
#             check = input('что хотите удалить?')
#             del workers[fio][check]
#             print('данные были удалены')
#
#     elif command == 'find':
#         fio = input('Введите ФИО сотрудника у которого хотите найти')
#         chekk = input('1.показать полностью данные, 2. показать определенные данные')
#         if chekk == '1':
#             data = workers.get(fio)
#             print(data)
#
#         elif chekk == '2':
#             check = input('что хотите увидеть?')
#             data = workers[fio].get(check)
#             print(data)
#
#     elif command == 'exit':
#         break
#     command = input('Введите команду: add/replace/delete/find/exit')
#
# print(workers)