# class mashins:
#     def __init__(self):
#         self.transport = ' '
#
#     def vid_trans(self):
#         self.transport = 'наземный вид транспорта'
#         return self.transport
#
#
# class wheel_mashins(mashins):
#     def __init__(self):
#         mashins.__init__(self)
#
#     def wheel_vid_mashins(self):
#         self.transport = 'колесный транспорт'
#         return self.transport
#
#
# class gusli_mashins(wheel_mashins):
#     def __init__(self):
#         wheel_mashins.__init__(self)
#
#     def gusli_vid_mashins(self):
#         self.transport = 'гусеничный транспорт'
#         return self.transport
#
#
# class air_bag(wheel_mashins):
#     def __init__(self):
#         wheel_mashins.__init__(self)
#
#     def air_bag_vid_mashins(self):
#         self.transport = 'траспорт на воздушной подушке'
#         return self.transport
#
#
# m = mashins()
# m1 = wheel_mashins()
# m2 = gusli_mashins()
# m3 = air_bag()
#
# print(m.vid_trans())
# print(m1.wheel_vid_mashins())
# print(m1.vid_trans())
# print(m2.gusli_vid_mashins())
# print(m2.vid_trans())
# print(m3.air_bag_vid_mashins())
# print(m3.wheel_vid_mashins())
# print(m3.vid_trans())
#
# print(m2.transport)
# print(m1.transport)
# m3.wheel_vid_mashins()
# print(m3.transport)
# print(m2.transport)

#  *** *** ***

class Fraction:
    def __init__(self, num: int =  0 , den: int = 1):
        self.num = num
        self.den = den

    def reset(self):
        self.num = int(input('Введите новый числитель'))
        self.den = int(input('Введите новый знаменатель'))

    def sum(self, another: 'Fraction'):
        sh_den = self.den * another.den
        sh_num = self.num * another.den + another.num * self.den
        return Fraction(sh_num, sh_den)

    def min(self, another: 'Fraction'):
        sh_den = self.den * another.den
        sh_num = self.num * another.den - another.num * self.den
        return Fraction(sh_num, sh_den)

    def umn(self, another: 'Fraction'):
        sh_den = self.den * another.den
        sh_num = self.num * another.num
        return Fraction(sh_num, sh_den)

    def dell(self, another: 'Fraction'):
        sh_den = self.den * another.num
        sh_num = self.num * another.den
        return Fraction(sh_num, sh_den)


pop = Fraction(3,4)
pip = Fraction(1,4)

c = pop.sum(pip)
print(c.num, c.den)

c1 = pop.min(pip)
print(c1.num, c1.den)

c2 = pop.umn(pip)
print(c2.num, c2.den)

c3 = pop.dell(pip)
print(c3.num, c3.den)
