# ZD_1
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.longerad = radius * 2 * 3.14
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __add__(self, other: 'Circle'):
#         result = Circle(self.radius + other.radius)
#         return result
#
#     def __sub__(self, other: 'Circle'):
#         result = Circle(self.radius - other.radius)
#         return result
#
#     def __str__(self):
#         return f'Радиус: {self.radius}'\
#                f'\nДлина окружности: {self.longerad}'
#
#     def __iadd__(self, num):
#         result = Circle(self.radius + num)
#         return result
#
#     def __isub__(self, num):
#         result = Circle(self.radius - num)
#         return result
#
# pop = Circle(6)
# pap = Circle(5)
# print(pop == pap)
# print(pop > pap)
# print(pop < pap)
# print(pop >= pap)
# print(pop <= pap)
# print(pop+pap)
# print(pop-pap)
# pap+= 5
# print(pap)

# ZD_2

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.real)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.real )

    def __mul__(self, other):
        return Complex(self.real * other.real - (self.imag * other.imag), self.imag * other.real + other.imag * self.real)

    def __lt__(self, other):
        return self.real + self.imag < other.real + other.imag

    def __gt__(self, other):
        return self.real + self.imag > other.real + other.imag

    def __le__(self, other):
        return self.real + self.imag <= other.real + other.imag

    def __ge__(self, other):
        return self.real + self.imag >= other.real + other.imag

    def __iadd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f'{self.real} + {self.imag}i'

a = Complex(4, 8)
b = Complex(6, 9)
print(a, b)
print(a+b)
print(a*b)


# ZD_3

# class Airplaine:
#
#     def __init__(self, model, number_place, passajir):
#         self.model = model
#         self.number_place = number_place
#         self.passajir = passajir
#
#     def __iadd__(self, num):
#         result = Airplaine(self.model, self.number_place, self.passajir + num)
#         return result
#
#     def __isub__(self, num):
#         result = Airplaine(self.model, self.number_place, self.passajir - num)
#         return result
#
#     def __eq__(self, other:'Airplaine'):
#         return self.model == other.model
#
#     def __lt__(self, other:'Airplaine'):
#         return self.number_place < other.number_place
#
#     def __gt__(self, other:'Airplaine'):
#         return self.number_place > other.number_place
#
#     def __le__(self, other:'Airplaine'):
#         return self.number_place <= other.number_place
#
#     def __ge__(self, other:'Airplaine'):
#         return self.number_place >= other.number_place
#
#     def __str__(self):
#         return f'Модель: {self.model}'\
#                f'\nКоличество мест: {self.number_place}'\
#                f'\nКоличество пассажиров: {self.passajir}'
#
#
# pop = Airplaine('koy', 50, 7)
#
# pop += 6
# pop -= 10
#
# print(pop)
#
#
# pap = Airplaine('koy', 65, 5)
#
# print(pop == pap)
# print(pop > pap)
# print(pop < pap)
# print(pop >= pap)
# print(pop <= pap)
#
# pap += 5
# print(pap)