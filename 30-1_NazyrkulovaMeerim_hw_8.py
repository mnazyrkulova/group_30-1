import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def create_country(conn, countr:tuple):
    try:
        sql = '''INSERT INTO countries(title) VALUES (?)'''
        cursor = conn.cursor()
        cursor.execute(sql, countr)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def create_city(conn, city:tuple):
    try:
        sql = '''INSERT INTO cities(title, area, country_id) VALUES (?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, city)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def create_employee(conn, employee:tuple):
    try:
        sql = '''INSERT INTO employees (fisrt_name, last_name, city_id) VALUES (?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)
db = 'homework_8.db'


create_table_countries = 'CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL)'
create_table_cities = '''CREATE TABLE cities(
id INTEGER PRIMARY KEY AUROINCREMENT,
title TEXT NOT NULL,
area DOUBLE(10, 2) DEFAULT 0,
country_id INTEGER, 
FOREIGN KEY (country_id) REFERENCES countries(id)
)'''

create_table_employees = '''CREATE TABLE employees(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES cities(id)
)'''

connection = create_connection(db)
create_table(connection, create_table_countries)
create_table(connection, create_table_cities)
create_table(connection, create_table_employees)
create_country(connection, create_table_countries)
# create_country(connection,('USA'))
# create_country(connection,('Germany'))
# create_country(connection,('Japan'))

create_city(connection, ('Washington', 1))
# create_city(connection, ('New-York', 1))
# create_city(connection, ('Berlin', 2))
# create_city(connection, ('Munchen', 2))
# create_city(connection, ('Osaka', 3))
# create_city(connection, ('Tokyo', 3))
# create_city(connection, ('Chicago', 1))

create_employee(connection, ('Mike', 'Wazowski', ))
# create_employee(connection, ('Lewis', 'Hamilton', )),
# create_employee(connection, ('Martin', 'Weber', )),
# create_employee(connection, ('Hiro', 'Tanaka', )),
# create_employee(connection, ('Klaus', 'Schmidt', )),
# create_employee(connection, ('Roman', 'Williams', )),
# create_employee(connection, ('Kira', 'Knightly', )),
# create_employee(connection, ('Eva', 'Simons', )),
# create_employee(connection, ('Rose', 'Depp', )),
# create_employee(connection, ('Arina', 'Takamoto', )),
# create_employee(connection, ('Lena', 'Berger', )),
# create_employee(connection, ('Takashi', 'Ino', )),
# create_employee(connection, ('David', 'Collins', )),
# create_employee(connection, ('Sara', 'Hans', )),
# create_employee(connection, ('Tao', 'Matsuoka', ))

def employees_in_city_id():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()
    city_id = int(input('Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:'))
    for city in cities:
        print(city[0], city[1])
        if city_id == 0:
            break
        cursor.execute('SELECT employees.first_name, employees.last_name, coutries.title, cities.title FROM employess'
                       'JOIN cities ON employees.city_id=cities_id JOIN countries ON cities.country_id=coutries_id'
                       'WHERE cities_id=?, (city_id,)'
                       )
        employees = cursor.fetchall()
        for employee in employees:
            print(employee[0], employees[1], employee[2])
            employees_in_city_id()