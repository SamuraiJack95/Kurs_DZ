import json

class Shoes:
    def __init__(self, type_shoes, view_shoes, color, price, producer, size):
        self.type_shoes = type_shoes
        self.view_shoes = view_shoes
        self.color = color
        self.price = price
        self.producer = producer
        self.size = size

    def __str__(self):
        return f'{self.type_shoes} - {self.view_shoes}'


class ShoesModel:
    def __init__(self):
        self.filepath = 'db.txt'
        try:
            # не понимаю как изменить название массива так чтобы небыло бесконечной интерации
            self.shoeses = json.load(open(self.filepath, 'rt', encoding= 'utf-8'))
            for shoes in self.shoeses.values():
                self.shoeses[shoes['type_shoes']] = Shoes(*shoes.values())
        except json.decoder.JSONDecodeError:
            self.shoeses = {}
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')
            self.shoeses = {}

    # Проблема в представлении словаря. Ошибка говорит что нет атрибутов, пробовал много раз менять
    # так и не нашел рабочего способа как нормально сделать можете помочь?



    def add_shoes(self, shoes):
        self.shoeses[shoes['тип обуви']] = Shoes(*shoes.values())
        for i in self.shoeses.items():
            print(i[0], i[1])

        dict_shoeses = {shoes.type_shoes: shoes.__dict__ for shoes in self.shoeses.values()}
        json.dump(dict_shoeses, open(self.filepath, 'wt', encoding='utf-8'))

        # shoes = Shoes(*shoes.values())
        # self.shoeses[shoes.view_shoes] = shoes.__dict__
        # json.dump(self.shoeses, open(self.filepath, 'wt', encoding='utf-8'))

    def get_all_shoeses(self):
        return self.shoeses