

class ShoesView:

    def wait_user_answer(self):
        print('Ожидание пользовательского ввода'.center(50, '='))
        print('Возможности действий:'
              '\n1. Добавить обувь'
              '\n2. Показать всю обувь'
              '\n"quit" - выход из программы')
        user_query = input('Введите вариант действия: 1.')
        print('=' * 50)
        return user_query

    def add_user_shoes(self):
        dict_shoes = {'тип обуви': None,
                      'вид обуви': None,
                      'цвет': None,
                      'цена': None,
                      'производитель': None,
                      'размер': None}
        print('создание обуви'.center(50, '='))
        for key in dict_shoes:
            dict_shoes[key] = input(f'Введите {key} обуви')
        print('=' * 50)
        return dict_shoes

    def print_all_shoeses(self, shoeses):
        print('список обуви'.center(50, '='))
        for index, shoes in enumerate(shoeses.values(), start = 1):
            print(f'{index}.{shoes}')
        print('=' * 50)