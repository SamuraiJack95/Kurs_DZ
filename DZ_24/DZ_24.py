# ZD_1
#
# isk = ['a', 'o', 'i', 'u', 'y', 'e']
#
# mas = 'ggghhhiiiooohhhaaa'
#
# pip = lambda lst: [x for x in lst if x not in isk ]
#
# print(''.join(pip(mas)))

# ZD_2

# isk = ['/', '.', ',', ':', ';']
# pip = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# mas = ['fgfgfdd12', 'dd', '123', '.,rr33', '/.', 'ed12er/.']
#
# fgh = lambda lst: [pap for pap in mas if not ([hoh for hoh in pap if (hoh in isk or hoh in pip)])]
#
# print(fgh(mas))

# ZD_3

# import functools
#
# mas = [1, 4, 5, 6, 9]
#
# gog = functools.reduce(lambda x, y: x*y, mas)
#
# print(gog)

# ZD_4

# не могу придумать как можно написать эту функцию можете подсказать?
# Можем.
# Напишите лямбда-функцию, которая принимает
# список строк и возвращает новый
# список, содержащий только строки,
# являющиеся палиндромами.
                                                                      #тут при проверке удаляем все пробелы и обе строки уменьшаем к нижнему регистру
is_palindrom = lambda strings: [string for string in strings if string.replace(' ', '').lower() == string[::-1].replace(' ', '').lower()]
                                                                      #а с помощью среза [::-1] переворачиваем саму строку, таким образом в итоговом массиве будут только строки палиндромы
print('Введите число')

# mas = int(input())
# for i in range(mas+1):
#     kok = lambda k,i, mas: k+1 for i in range(mas) if i % x == 0

# print(kok(mas))
