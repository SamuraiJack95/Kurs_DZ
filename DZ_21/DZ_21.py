# ZD_1

# class phonenumber:
#     def __init__(self):
#         self.dictnumb = {}
#
#
#     def dictnumb_add(self, name, number):
#         self.dictnumb[name] = number
#         print('добавлен контакт')
#
#
#     def remove_number(self, name):
#         if name in self.dictnumb.keys():
#             del self.dictnumb[name]
#             print('контакт удален')
#         else:
#             print('такого контакта нет')
#
#
#     def update_dictnumb(self, name, number):
#         if name in self.dictnumb.keys():
#             self.dictnumb[name] = number
#         else:
#             print('Такого контакта нет')
#
#
#     def get_dictnumb(self, name):
#         return self.dictnumb[name]
#
#
#     def getall_dictnumb(self):
#         dictmas = []
#         for key, value in self.dictnumb.items():
#             dictmas.append([key, value])
#         return dictmas
#
#
# dict1 = phonenumber()
#
# dict1.dictnumb_add('Maxim', '+7 927 709 99 87')
#
# print(dict1.getall_dictnumb())
# print(dict1.get_dictnumb('Maxim'))
#
# dict1.dictnumb_add('Sergey', '+7 965 456 78 45')
# dict1.remove_number('Maxim')
# dict1.update_dictnumb('Sergey', '5678')
# dict1.update_dictnumb('Maxim', '54432')
#
# print(dict1.getall_dictnumb())

# ZD_2

import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.fin_time = 0

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            print('Таймер фигачит')

    def stop(self):
        if self.start_time is not None:
            self.fin_time = time.time() - self.start_time

    def reset(self):
        self.start_time = None

    def result_time(self):
        if self.start_time:
            return time.time() - self.start_time
        return 'Таймер бро не запущен'


time1 = Timer()
time1.start()
[i for i in range(10000000)]
time1.stop()

print(time1.result_time())
