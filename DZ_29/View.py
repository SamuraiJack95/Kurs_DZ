def add_title(title):
    def decor(func):
        def wrapper(*args,**kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result
        return wrapper
    return decor

class ShoesView:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('Возможности действий:'
              '\n1. Добавить обувь'
              '\n2. Показать всю обувь'
              '\n3. Показать нужную обувь'
              '\n4. Удалить обувь'
              '\n"quit" - выход из программы')
        user_query = input('Введите вариант действия: 1.')
        return user_query

    @add_title('создание обуви')
    def add_user_shoes(self):
        dict_shoes = {'тип обуви': None,
                      'вид обуви': None,
                      'цвет': None,
                      'цена': None,
                      'производитель': None,
                      'размер': None}
        for key in dict_shoes:
            dict_shoes[key] = input(f'Введите {key} обуви')
        return dict_shoes

    @add_title('список обуви')
    def print_all_shoeses(self, shoeses):
        for index, shoes in enumerate(shoeses.values(), start = 1):
            print(f'{index}.{shoes}')

    @add_title('Ввод название модели обови')
    def get_user_shoes(self):
        user_shoes = input('Введите вам нужную обувь')
        return user_shoes

    @add_title('Просмотр обуви')
    def show_single_shoes(self, shoes):
        if isinstance(shoes, dict) and -1 in shoes:
            print(shoes[-1])
            return
        list_shoes = ['тип обуви',
                      'вид обуви',
                      'цвет',
                      'цена',
                      'производитель',
                      'размер']
        for key, value in zip(list_shoes, shoes.__dict__.values()):
            print(f'{key} обувь - {value}')

    @add_title('удаление статьи')
    def get_result_del(self, result_code):
        if result_code == 0:
            print('Удаление прошло успешно')
        elif result_code == -1:
            print('Такой обуви не существует')


