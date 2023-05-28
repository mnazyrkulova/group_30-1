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

def insert_product(conn, product):
    sql = '''
    INSERT INTO products(product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product(conn, product):
    sql = '''
    UPDATE products SET price = ?, quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''
    DELETE FROM students WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def select_all_products(conn):
    sql = ''' SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)


def select_products_by_price_and_quantity_limit(conn, limit):
    sql = ''' SELECT * FROM products WHERE price >= ? and quantity >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit, ))
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)

connect = create_connection('hw.db')

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL 0)
'''

if connect is not None:
    print('Connected successfuly')
    create_table(connect, sql_create_products_table)
    insert_product(connect, ('Чипсы Lays', 135, 56))
    insert_product(connect, ('Чипсы Pringles ', 180, 40))
    insert_product(connect, ('Чипсы Пир', 85, 4))
    insert_product(connect, ('Чипсы Lays Beer Flavor', 140, 18))
    insert_product(connect, ('Чипсы Kracks', 178, 24))
    insert_product(connect, ('Крекеры классические', 40, 57))
    insert_product(connect, ('Крекеры сырные', 45, 55))
    insert_product(connect, ('Крекеры с паприкой', 48, 34))
    insert_product(connect, ('Шоколад Toblerone', 230, 2))
    insert_product(connect, ('Шоколад Alpen Gold', 60, 3))
    insert_product(connect, ('Крекеры Tuc', 70, 8))
    insert_product(connect, ('Шоколад Milka', 92, 18))
    insert_product(connect, ('Шоколад Аленка', 220, 10))
    insert_product(connect, ('Шоколад RieterSport', 120, 25))
    insert_product(connect, ('Шоколад Merci ', 315, 22))

    select_all_products(connect)
    select_products_by_price_and_quantity_limit(connect, )
    update_product(connect(195, 24, 2))
    delete_product(connect, 3)
    connect.close()