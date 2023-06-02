import threading
import random

# ZD_1
#
# list_1 = []
# a = int(input('введите количество рандомных чисел'))
# def rand_ch(a):
#     for i in range(a):
#         k = random.randint(1, 10)
#         list_1.append(k)
#     print(list_1)
#
# def summ(s):
#     su = sum(s)
#     print(su)
#
# def sred(d):
#     srd = sum(d)/len(d)
#     print(srd)
#
# thd_1 = threading.Thread(target=rand_ch, args=(a,))
# thd_2 = threading.Thread(target=summ, args=(list_1,))
# thd_3 = threading.Thread(target=sred, args=(list_1,))
#
# thd_1.start()
# thd_2.start()
# thd_3.start()
# thd_2.join()
# thd_3.join()
#
# print('programm is fin')

# ZD_2

# file_1 = input('введите имя файла')
# def load_fail(file_1):
#
#     with open(file_1, 'w') as f1:
#         for i in range(100):
#             f1.write('{}\n'.format(random.randint(1,10)))
#
# def prost(file_1):
#     with open(file_1, 'r') as f2:
#         listt = [int(word) for word in f2.read().split()]
#         llist = []
#     k = 0
#     for i in listt:
#         for y in range(2, i // 2 + 1):
#             if (i % y == 0):
#                 k = k + 1
#         if (k <= 0):
#             llist.append(i)
#         k = 0
#     with open('file_2.txt', 'w') as f2:
#         f2.write(str(llist))
#
# def factorial(file_1):
#     with open(file_1, 'r') as f2:
#         listtt = [int(word) for word in f2.read().split()]
#     lliist = []
#     fact = 1
#     for l in listtt:
#         for num in range(2, l + 1):
#             fact *= num
#         lliist.append(fact)
#         fact = 1
#     with open('file_3.txt', 'w') as f3:
#         f3.write(str(lliist))
#
# thd_1 = threading.Thread(target=load_fail, args=(file_1,))
# thd_2 = threading.Thread(target=prost, args=(file_1,))
# thd_3 = threading.Thread(target=factorial, args=(file_1,))
#
# thd_1.start()
# print('programm is start')
# thd_2.start()
# print('programm go')
# thd_3.start()
# thd_2.join()
# thd_3.join()
#
# print('programm is fin')

# ZD_3

# не очень понял задание про потоки, сказано что одним потоком перенести файлы, сделал как понял это задание.

import shutil
import os

# пути к деректориям
# C:/KursPython/Kurs_DZ/DZ_33/ZD1/
# C:/KursPython/Kurs_DZ/DZ_33/ZD2


file_source =input('введите путь к деректории файлов')
file_destination =input('введите деректорию куда перенести файлы')
def move_fail(file_source, file_destination):

    get_files = os.listdir(file_source)

    for g in get_files:
        shutil.move(file_source + g, file_destination)


thd_1 = threading.Thread(target=move_fail, args=(file_source,file_destination))
thd_1.start()
print('programm is fin')

# 4 задание не сделал, мало времени, как можно быстрее пытаюсь закрыть долги перед проектом.