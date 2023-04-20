import json

class Shape:

    def __init__(self, cor):
        self.cor = cor


    def show(self):
        print(f'Фигура{self.__class__.__name__}')
        print('Её свойства: ')
        for name, value in self.__dict__.items():
            print(f'{name} = {value}')

    @staticmethod
    def save(file_pip):
        data = (?).__dict__
        with open("file_pip.json", "w") as write_file:
            json.dump(data, write_file)

    @staticmethod
    def load(file_pip):
        with open("file_pip.json", "r") as read_file:
            data = json.load(read_file)

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
a.save('pip.txt')