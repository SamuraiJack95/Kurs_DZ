# ZD_1
#
# class Fraction:
#     counter = 0
#
#     def __init__(self, num: int = 0, den: int = 1):
#         self.num = num
#         self.den = den
#         Fraction.counter += 1
#
#     def reset(self):
#         self.num = int(input('Введите новый числитель'))
#         self.den = int(input('Введите новый знаменатель'))
#
#     def sum(self, another: 'Fraction'):
#         sh_den = self.den * another.den
#         sh_num = self.num * another.den + another.num * self.den
#         return Fraction(sh_num, sh_den)
#
#     def min(self, another: 'Fraction'):
#         sh_den = self.den * another.den
#         sh_num = self.num * another.den - another.num * self.den
#         return Fraction(sh_num, sh_den)
#
#     def umn(self, another: 'Fraction'):
#         sh_den = self.den * another.den
#         sh_num = self.num * another.num
#         return Fraction(sh_num, sh_den)
#
#     def dell(self, another: 'Fraction'):
#         sh_den = self.den * another.num
#         sh_num = self.num * another.den
#         return Fraction(sh_num, sh_den)
#
#     @staticmethod
#     def countter_obj():
#         return Fraction.counter
#
# pop = Fraction(3,4)
# pip = Fraction(1,4)
#
# c = pop.sum(pip)
# print(c.num, c.den)
#
# c1 = pop.min(pip)
# print(c1.num, c1.den)
#
# c2 = pop.umn(pip)
# print(c2.num, c2.den)
#
# c3 = pop.dell(pip)
# print(c3.num, c3.den)
#
# print(f'{Fraction.countter_obj()}')


# ZD_2

# F = 9/5 * C + 32
# C = (F - 32) * 5/9

# class Convector:
#     counter_c = 0
#     counter_f = 0
#
#     def __init__(self, cel, frg):
#         self.cel = cel
#         self.frg = frg
#
#     @staticmethod
#     def frg_cel(frgg):
#         cell = (frgg - 32) * 5/9
#         Convector.counter_f += 1
#         return cell
#
#     @staticmethod
#     def cel_frg(celll):
#         ffrg = (9/5) * celll + 32
#         Convector.counter_c += 1
#         return ffrg
#
#     @staticmethod
#     def counters_opers():
#         return  Convector.counter_c, Convector.counter_f
#
# m1 = Convector.cel_frg(10)
# m2 = Convector.frg_cel(50)
# m3 = Convector.cel_frg(30)
# m4 = Convector.frg_cel(40)
# m5 = Convector.cel_frg(70)
#
# print(m1, m2, m3, m4, m5)
#
# print(f'{Convector.counters_opers()}')

# ZD_3

# mil = m / 1609m
# m = mil * 1609m
# funt = gr/ 453gr
# gr = funt * 453gr
# akr = km^2 / 4046 km^2
# km^2 = akr * 4046 km^2

class Eng_convector:
    counter_oper = 0

    @staticmethod
    def mil_m(m):
        Eng_convector.counter_oper += 1
        mil = m / 1609
        return mil

    @staticmethod
    def m_mil(mi):
        Eng_convector.counter_oper += 1
        met = mi * 1609
        return met

    @staticmethod
    def funt_gram(funt):
        Eng_convector.counter_oper += 1
        gram = funt * 453
        return gram

    @staticmethod
    def gram_funt(gra):
        Eng_convector.counter_oper += 1
        funt = gra / 453
        return funt

    @staticmethod
    def km_akr(kmm):
        Eng_convector.counter_oper += 1
        akr = kmm / 4046
        return akr

    @staticmethod
    def akr_km(akrr):
        Eng_convector.counter_oper += 1
        kkm = akrr * 4046
        return kkm

    @staticmethod
    def counter_operations():
        return Eng_convector.counter_oper

print(Eng_convector.mil_m(100))
print(Eng_convector.mil_m(1000))
print(Eng_convector.m_mil(10))
print(Eng_convector.m_mil(1))
print(Eng_convector.funt_gram(10))
print(Eng_convector.funt_gram(1))
print(Eng_convector.gram_funt(100))
print(Eng_convector.gram_funt(1000))
print(Eng_convector.km_akr(100))
print(Eng_convector.km_akr(10000))
print(Eng_convector.akr_km(1))
print(Eng_convector.akr_km(10))
print(Eng_convector.counter_operations())

