import json

# class Loadsave:
#     def __init__(self):
#         self.data = {}
#         self.filepath = 'pip.txt'
#
#     def save(self):
#         self.data[class]
#     # def add_shoes(self, shoes):
#     #     self.shoeses[shoes['тип обуви']] = Shoes(*shoes.values())
#     #     # for i in self.shoeses.items():
#     #     #     print(i[0], i[1])
#     #
#     #     dict_shoeses = {shoes.type_shoes: shoes.__dict__ for shoes in self.shoeses.values()}
#     #     json.dump(dict_shoeses, open(self.filepath, 'wt', encoding='utf-8'))
#
#     def load(self):
#         pass
#
#         # self.shoeses ={}
#         #             self.shoesess = json.load(open(self.filepath, 'rt', encoding= 'utf-8'))
#         #             for shoes in self.shoesess.values():
#         #                 self.shoeses[shoes['type_shoes']] = Shoes(*shoes.values())
#
class Shape:

    def __init__(self, cor):
        self.cor = cor
        self.cls = self.__class__.__name__

    def show(self):
        print(f'Фигура{self.__class__.__name__}')
        print('Её свойства: ')
        for name, value in self.__dict__.items():
            print(f'{name} = {value}')


    def save(self, file_pip):
        data = self.__dict__
        with open(file_pip, "at") as write_file:
            json.dump(data, write_file)


    def load(self, file_pip):
        with open(file_pip, "r") as read_file:
            data = json.load(read_file)
            for obj in data:
                for atr in obj:
                    if atr == self.cls:
                        return __class__.__name__(*obj.values())


class Square(Shape):

    def __init__(self, cor, stor):
        Shape.__init__(self, cor)
        self.stor = stor



class Rectagle(Shape):

    def __init__(self, cor, long, width ):
        Shape.__init__(self, cor)
        self.long = long
        self.width = width


class Circle(Shape):

    def __init__(self, cor, rad):
        Shape.__init__(self, cor)
        self.rad = rad


a = Circle(4,5)
b = Square(6,7)
a.save('pip.txt')
b.save('pip.txt')

c = Square.load('pip.txt', Square)








