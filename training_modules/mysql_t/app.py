from re import L
from mysql.connector import connect, Error
from getpass import getpass

try:
    with connect(
        host='localhost',
        user=input('Input login: '),
        password=getpass('Input password: ')
    ) as connection:
        conn = connection
except Error as e:
    print(e)

