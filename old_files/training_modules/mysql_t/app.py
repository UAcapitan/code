from mysql.connector import connect, Error
from getpass import getpass

try:
    with connect(
        host='127.0.0.1',
        user=input('Input login: '),
        password=getpass('Input password: ')
    ) as connection:
        conn = connection
        create_db_query = "CREATE DATABASE data_of_something"
        with conn.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

