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
        return f'{self.type_shoes} - {self.view_shoes} - {self.producer}'


class ShoesModel:
    def __init__(self):
        self.filepath = 'db.txt'
        try:
            self.shoeses ={}
            self.shoesess = json.load(open(self.filepath, 'rt', encoding= 'utf-8'))
            for shoes in self.shoesess.values():
                self.shoeses[shoes['type_shoes']] = Shoes(*shoes.values())
        except json.decoder.JSONDecodeError:
            self.shoeses = {}
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')
            self.shoeses = {}

    def add_shoes(self, shoes):
        self.shoeses[shoes['тип обуви']] = Shoes(*shoes.values())
        # for i in self.shoeses.items():
        #     print(i[0], i[1])

        dict_shoeses = {shoes.type_shoes: shoes.__dict__ for shoes in self.shoeses.values()}
        json.dump(dict_shoeses, open(self.filepath, 'wt', encoding='utf-8'))

    def get_all_shoeses(self):
        return self.shoeses

    def get_single_shoes(self, shoes_name):
        try:
            return self.shoeses[shoes_name]
        except KeyError:
            return {-1: self.missing_shoes_warning(shoes_name)}

    def missing_shoes_warning(self, shoes_name):
        return f'Ошибка: не существует обуви с названием {shoes_name}'

    def delete_shoes(self, shoes_name):
        try:
            del self.shoeses[shoes_name]
            return 0
        except KeyError:
            return -1

