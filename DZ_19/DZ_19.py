import json

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

        with open(file_pip, "at") as f:
            json.dump({self.__class__.__name__:self.__dict__},f)

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            obj = json.load(f)
            cls_name = list(obj.keys())[0]
            for subcls in Shape.__subclasses__():
                if subcls.__name__ == cls_name:
                    return subcls(**list(obj.values())[0])


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


# a = Circle(4,5)
# b = Square(6,7)
# a.save('pip.txt')
# b.save('pip.txt')
# b.load('pip.txt')

# понимаю что не доконца доделал, но уже много времени убил на это, а заданий много, поэтому сдаю таким, извините
# можете показать что тут доделать нужно чтобы работало? чтобы разобраться позже с этим заданием уже чисто для себя
# в целом я понял это задание, но нехватило сил и времени доделать.




