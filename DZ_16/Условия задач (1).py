# 1.

# Дан массив strs буквенно-цифровых строк,
# вернуть максимальное значение любой строки в strs
#
# Значение буквенно-цифровой строки
# может быть определено как:
#
# Числовое представление строки с основанием 10,
# если оно состоит только из цифр.
# Длина строки, в противном случае.
#
# >>> ["alic3","bob","3","4","00000"]
#         5      3    3   4     0
#
# <<< 5


# 2.

# Дан массив строк. Вернуть все строки
# в словах, которые являются
# подстрокой любой другой строки.
# Вы можете вернуть ответ в любом порядке.
#
# Подстрока — это непрерывная последовательность
# символов в строке
#
# >>> ["mass","as","hero","superhero"]
#
# <<< ["as", "hero"]

# 3.

# Вам даны два массива строк, которые
# представляют два события.
# События(event1 и event2) произошли
# в один и тот же день, где:
#
# event1 = [startTime1, endTime1] и
# event2 = [startTime2, endTime2].
# Время события действительно в 24-часовом
# формате в формате ЧЧ:ММ.
#
# Конфликт возникает, когда два события
# имеют некоторое непустое пересечение
# (т. е. какой-то момент является общим для обоих событий).
#
# Верните True, если есть конфликт между двумя
# событиями. В противном случае верните False.
#
# >>> ["01:15", "02:00"] ["02:00","03:00"]
#
# <<< True

# 4.

# Вам дан массив целых чисел heights,
# представляющий текущий порядок,
# в котором стоят ученики.
#
# Каждое heights[i] — это рост i-го ученика
# в очереди.
#
# Ученики стоят в случайном порядке, но для
# фотографии они должны стоять по неубыванию
# (мягкому возрастанию: 1, 1, 2, 3, 3, 3, 4)
#
# Верните количество индексов,
# где heights[i] != ожидаемый[i].
# Иными словами, количество учеников,
# которые стоят не на своих местах.
# >>> [1,1,4,2,1,3] (правильный порядок):
#     [1,1,1,2,3,4]
# <<< 3


# 5.

# Дано целое число numRows,
# вернуть первые numRows треугольника Паскаля.
#
# В треугольнике Паскаля каждое число
# является суммой двух чисел непосредственно
# над ним, как показано:
#
#           |1|
#          |1||1|
#         |1||2||1|
#        |1||3||3||1|
#       |1||4||6||4||1|


# 6.

# Дан массив целых чисел,
# отсортируйте массив в порядке
# возрастания в зависимости от
# частоты значений.
#
# Вернуть отсортированный массив.
#
# lst = [2, 1, 2, 2, 1, 3] => [3, 1, 1, 2, 2, 2]


# 7.

# Вам дан массив nums, состоящий
# из целых положительных чисел.
#
# Вы должны взять каждое целое число
# в массиве, поменять местами его цифры
# и добавить новое число в конец массива.
#
# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.


# 8.

# Дан массив целых чисел nums.
# Верните максимальное значение такое, что:
# (nums[i]-1)*(nums[j]-1).
