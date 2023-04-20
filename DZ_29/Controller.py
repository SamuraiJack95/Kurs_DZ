from Model import ShoesModel
from View import ShoesView
from Model import Shoes

class ShoesController:
    def __init__(self):
        self.model = ShoesModel()
        self.view = ShoesView()

    def run(self):
        print('Ожидание пользовательского ввода'.center(50, '='))
        query = None
        while query != 'quit':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, answer):
        if answer == '1':
            values = self.view.add_user_shoes()
            self.model.add_shoes(values)
        elif  answer == '2':
            shoeses = self.model.get_all_shoeses()
            self.view.print_all_shoeses(shoeses)
        elif answer == '3':
            shoes_name = self.view.get_user_shoes()
            shoes = self.model.get_single_shoes(shoes_name)
            self.view.show_single_shoes(shoes)
        elif answer == '4':
            shoes_name = self.view.get_user_shoes()
            result_code = self.model.delete_shoes(shoes_name)
            self.view.get_result_del(result_code)