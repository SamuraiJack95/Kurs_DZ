# 1
from abc import ABC, abstractmethod

class Commanderjojo(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def process(self):
        pass

class CommanderImpl(Commanderjojo):
    def process(self):
        self.receiver.per_act()

class Receiver:
    def per_act(self):
        print('Hei Mark!)')

class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()

rec = Receiver()
cmd = CommanderImpl(rec)
inv = Invoker()
inv.command(cmd)
inv.execute()


# ZD_2
#
# import time
# import random
#
# class Number:
#     def __init__(self):
#         self.__nums = [random.randint(1, 10) for i in range(10)]
#         self.logger = Proxylogger('file.txt')
#
#
#     @property
#     def nums(self):
#         self.logger.note()
#         return self.__nums
#
#     def summa(self):
#         self.logger.note()
#         print('jojo')
#         return sum(self.__nums)
#
#     def maxi(self):
#         self.logger.note()
#         print('dio')
#         return max(self.__nums)
#
#     def mini(self):
#         self.logger.note()
#         print('stolp')
#         return min(self.__nums)
#
#
# class Proxylogger:
#     def __init__(self, file):
#         self.file = file
#
#     def note(self):
#         with open(self.file, 'a', encoding='utf-8') as f:
#             f.write(f'\nNumbers ehoo заюзан {time.gmtime()}')
#
# a = Number()
#
# print(a.maxi())
# print(a.mini())
# print(a.summa())