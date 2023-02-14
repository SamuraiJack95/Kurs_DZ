# zd_6

# mas1 = [5, 5, 2, 2, 2, 1, 1, 1, 1]
# count_mas = {}
# count = 0
#
# for i in mas1:
#     count_mas.append(mas1.count(i))
#
#
# print(count_mas)

#

# никак не могу додумать принцип

# zd_7

mas1 = [3456, 6543, 34, 876]


for i in mas1:
    elem = str(mas1.pop(0))
    elemmas = list(elem)
    elemmas.reverse()
    elemm = "".join(elemmas)
    mas1.append(elemm)

print(mas1)

print(elemmas)

# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.

# не очень понял формулировку задания, они и так все уникальные, если надо менять
# числа с любыми местами, не могу понять какой нужен тогда подход помогите разобрать

