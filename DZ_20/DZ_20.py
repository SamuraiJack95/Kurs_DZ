# DZ_6

# def notmin(func):
#     def minmin(*args):
#         result = func(*args)
#         if result < 0:
#             print(f'результат был изменен на 0, было отрицательное число {result} ')
#             result = 0
#         return result
#     return minmin
#
# @notmin
# def summ(*args):
#     return sum(args)
#
# print(summ(6, 9, (-65),100))

# DZ_7

import random

def retry(num):
    def decor(func):
        def basd_fun(*args):
            for i in range(num):
                try:
                    return func(*args)
                except Exception:
                    if i == num - 1:
                        raise Exception
        return basd_fun
    return decor


@retry(num=1)
def get_ran():
    if random.randint(0,1):
        raise ValueError('Функция капут')
    return 'Все чики-брики'

print(get_ran())

