# DZ_12

# ZD_1

# with open(file = 'JOJO.txt', mode = 'r', encoding = 'UTF-8') as f1:
#     mas1 = list(f1.read().split('\n'))
#
# with open(file='DIO.txt', mode= 'r', encoding = 'UTF-8') as f2:
#     mas2 = list(f2.read().split('\n'))
#
# with open(file='kek.txt', mode='w', encoding= 'UTF-8') as f3:
#     for i in range(len(mas2)):
#         if mas1[i] != mas2[i]:
#             f3.writelines(mas1[i] + '\n')
#             f3.writelines(mas2[i] + '\n')


# ZD_2
#
# number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# glas = ['a', 'o', 'u', 'y', 'e', 'i']
# punk = ['.', ',', ':', ';', '-', '\\n']
#
# with open(file='PIP.txt', mode='r', encoding='UTF-8') as f1:
#     sym = f1.read()
#     f1.seek(0)
#     st = len(f1.readlines())
#
# count_gl = 0
# count_sgl = 0
# count_num = 0
#
# for i in sym:
#     if i in glas:
#         count_gl += 1
#     elif i in number:
#         count_num += 1
#     elif (i not in glas) and (i not in number) and (i not in punk):
#         count_sgl += 1
#
# count_sgl = count_sgl - (st - 1)
# symm = len(sym) - (st - 1)
#
# count_sgl = str(count_sgl)
# count_num = str(count_num)
# count_gl = str(count_gl)
# symm = str(symm)
# st = str(st)
#
#
# res = "Кол-во символов = " + symm + "\n" + "Кол-во строк = " + st + "\n" + "Кол-во цифр = " + count_num + "\n" + "Кол-во гласных = " + count_gl + "\n""Кол-во согласных = " + count_sgl
#
#
#
# with open(file='pis.txt', mode='w', encoding='UTF-8') as f2:
#     f2.write(res)

# zd_3