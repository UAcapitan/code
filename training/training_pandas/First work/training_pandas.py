import pandas as pd
import csv
import json
import sqlite3

# Dict with data
data = {
    'appples': [3,2,1,0],
    'oranges': [7,4,3,1]
}

# And index
index = ['Ivan', 'Igor', 'Alex','Masha']

# Create DataFrame
purchares = pd.DataFrame(data, index=index)

# Output table DataFrame

# print(purchares, end="\n\n")
# print(purchares.loc['Ivan'])

# Create csv file
row_list = [
    ['apples', 'oranges'],
    [3,7],
    [2,4],
    [1,3],
    [0,1]
]

with open('files/purchares.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

# Create DataFrame with data from csv file
purchares_2 = pd.read_csv('files/purchares.csv')

# Output new DataFrame with data from csv file
# print(purchares_2)

# Create DateFrame with data from csv file without index
purchares_3 = pd.read_csv('files/purchares.csv', index_col=0)

# Output new DataFrame with data from csv file without index
# print(purchares_3)

# Create json file
with open('files/data.json', 'w') as outfile:
    json.dump(data, outfile)

# Create DateFrame with data from json
purchares_4 = pd.read_json('files/data.json')

# Output DateFrame with data from json
# print(purchares_4)

# Create new db sqlite3
conn = sqlite3.connect('files/new_db.db')
print(sqlite3.version)
c = conn.cursor()
# sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS purchares(
#                                         id integer PRIMARY KEY,
#                                         apples integer NOT NULL,
#                                         oranges integer NOT NULL
#                                     ); """
# c.execute(sql_create_projects_table)
# sql = ''' INSERT INTO purchares(apples,oranges)
#               VALUES(1,2) '''
# c.execute(sql)
# conn.commit()
conn.close()
print('db update now')

# Create DateFrame from db sqlite3
conn = sqlite3.connect('files/new_db.db')

purchares_5 = pd.read_sql_query('SELECT * FROM purchares', conn)

conn.close()

# Output DateFrame from db sqlite3
print(purchares_5)