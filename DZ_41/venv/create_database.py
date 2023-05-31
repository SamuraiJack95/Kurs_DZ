from faker import Faker

from DZ_41.models.database import create_db, Session
from DZ_41.models.customers import Customers
from DZ_41.models.sales import Sales
from DZ_41.models.salesmen import Salesmen
def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):
    faker = Faker('ru-RU')
    customersus = ['стенделон стенделонович', 'стеткхем стетхомич', 'ватрушка ватрушочная', 'оулсчит считович', 'джет пакович', 'волдан волданович']
    adrsas = ['москва', 'питер', 'самара', 'уркутск', 'стальград', 'кемерово']
    rey = [8, 7, 5, 6, 3, 8]
    salesmen_1 = Salesmen(full_name='гридачин максим васильев', adress='москва', reyting_pr=5)
    salesmen_2 = Salesmen(full_name='джонов джон джонович',adress='питер', reyting_pr=7)
    salesmen_3 = Salesmen(full_name='пупиркин пупырка пупыркович',adress='самара', reyting_pr=9)
    session.add(salesmen_1)
    session.add(salesmen_2)
    session.add(salesmen_3)

    cust_1= []

    for id_cus in range(5):
        cust = Customers(full_name=customersus[id_cus], adress=adrsas[id_cus], reyting_kl=rey[id_cus])
        if id_cus <= 1:
            cust.salesmens.append(salesmen_1.id_pr)
            cust_1.append(id_cus)
        elif id_cus <= 3:
            cust.salesmens.append(salesmen_2.id_pr)
            cust_1.append(id_cus)
        elif id_cus <= 5:
            cust.salesmens.append(salesmen_3.id_pr)
            cust_1.append(id_cus)

        session.add(cust)


    session.commit()
    prodd = ['ковер', 'ножницы', 'самокат', 'телевизор', 'монитор', 'бумага', 'чернила', 'труба', 'сигареты']
    addresss = ['москва', 'питер', 'самара', 'уральск', 'курск', 'екатеринбург']
    salos= [salesmen_1, salesmen_2, salesmen_3]
    for _ in range(50):
        summa = faker.random.randint(100, 100000)
        count_pr = faker.random.randint(1, 100)
        salo = faker.random.choice(salos)
        address = faker.random.choice(addresss)
        custt= faker.random.choice(cust_1)
        product = faker.random.choice(prodd)

        sales = Sales(salo.id, custt, summa, count_pr, address, product)
        session.add(sales)

    session.commit()
    session.close()


