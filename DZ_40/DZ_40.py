import sqlite3 as sq

# функция для перевода чисел в int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value

with sq.connect("emp.db") as con:
    cur = con.cursor()
    cur.executescript('CREATE TABLE IF NOT EXISTS EMP('
                      'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                      'MENEGER_ID INTEGER NOT NULL,'
                      'COUNTRY_ID INTEGER NOT NULL,'
                      'NAME TEXT NOT NULL,'
                      'LAST_NAME TEXT,'
                      'AGE INTEGER NOT NULL,'
                      'JOBS TEXT NOT NULL,'
                      'FOREIGN KEY (MENEGER_ID)  REFERENCES MENEGER (ID),'
                      'FOREIGN KEY (COUNTRY_ID)  REFERENCES COUNTRY (ID)'
                      ');')
    cur.executescript('CREATE TABLE IF NOT EXISTS MENEGER('
                      'ID INTEGER PRIMARY KEY,'
                      'NAME TEXT NOT NULL,'
                      'LAST_NAME TEXT,'
                      'AGE INTEGER NOT NULL,'
                      'JOBS TEXT NOT NULL'
                      ');')
    cur.executescript('CREATE TABLE IF NOT EXISTS COUNTRY('
                      'ID INTEGER PRIMARY KEY,'
                      'COUNTRY TEXT NOT NULL,'
                      'CONTINENT TEXT,'
                      'NUMBER_OF_EMPS INTEGER'
                      ');')
    # простой вид ввода данных
    mas = ()
    i = 0
    while i != "y":
        i = input('хотите продолжить нажмите 1,2,3 или y, чтобы закончить\n'
                  '1.Ввод в таблицу EMP\n'
                  '2.Ввод в таблицу MENEGER\n'
                  '3.Ввод в таблицу COUNTRY\n')
        if i == "y":
            break
        elif i == "1":
            print('Введите данные через пробел 5 столбцов\n'
                  '1.ID - число\n'
                  '2.MENEGER_ID - число\n'
                  '3.COUNTRY_ID - число\n'
                  '4.NAME - текст\n'
                  '5.LAST_NAME - текст\n'
                  '6.AGE - число\n'
                  '7.JOBS - текст\n')
            mas1 = input()
            # место где идет преобразование некоторых элементов списка из строки в число для базы
            # метод простой, неидеальный и имеет много условий и дыр, но для задания надеюсь сойдет
            mas = list(mas1.split(' '))
            mas = tuple(map(try_to_int, mas))
            print(mas)
            cur.executescript(f'INSERT INTO EMP VALUES({mas[0]}, {mas[1]}, {mas[2]}, "{mas[3]}", "{mas[4]}", {mas[5]}, "{mas[6]}")')


        elif i == "2":
            print('Введите данные через пробел 5 столбцов\n'
                  '1.ID - число\n'
                  '2.NAME - текст\n'
                  '3.LAST_NAME - текст\n'
                  '4.AGE - число\n'
                  '5.JOBS - текст\n')
            mas1 = input()
            mas = list(mas1.split(' '))
            mas = tuple(map(try_to_int, mas))
            print(mas)
            cur.executescript(f'INSERT INTO MENEGER VALUES({mas[0]}, "{mas[1]}", "{mas[2]}", {mas[3]}, "{mas[4]}")')


        elif i == "3":
            print('Введите данные через пробел 4 столбцов\n'
                  '1.ID - число\n'
                  '2.COUNTRY - текст\n'
                  '3.CONTINENT - текст\n'
                  '4.NUMVER_EMPS - число\n')
            mas1 = input()
            mas = list(mas1.split(' '))
            mas = tuple(map(try_to_int, mas))
            print(mas)
            cur.executescript(f'INSERT INTO COUNTRY VALUES({mas[0]}, "{mas[1]}", "{mas[2]}", {mas[3]})')


    cur.execute('SELECT * '
                'FROM EMP')
    print(cur.fetchall())

    cur.execute('SELECT E.NAME, E.LAST_NAME, M.ID, M.JOBS, C.COUNTRY '
                'FROM EMP  E, MENEGER M, COUNTRY C '
                'WHERE (E.MENEGER_ID = M.ID) AND (E.COUNTRY_ID = C.ID)')
    print(cur.fetchall())