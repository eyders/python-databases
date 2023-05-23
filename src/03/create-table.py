'''Crear tabla en la base de datos de postgres'''
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='manager',
    user='postgres',
    password='pgpassword'
)
cursor = connection.cursor()

CREATE_INVESTMENT_TABLE = """
create table investment (
    id serial primary key,
    coin varchar(32),
    currency varchar(3),
    amount real
)
"""

cursor.execute(CREATE_INVESTMENT_TABLE)
connection.commit()
cursor.close()
connection.close()
