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
# print(sqlite3.version)
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
# print('db update now')

# Create DateFrame from db sqlite3
conn = sqlite3.connect('files/new_db.db')

purchares_5 = pd.read_sql_query('SELECT * FROM purchares', conn)

conn.close()

# Output DateFrame from db sqlite3

# print(purchares_5)

# Sort by index
purchares_6 = purchares_5.set_index('id')

# Output index sort

# print(purchares_6)

# Convert DataFrames to csv, json, db

# conn = sqlite3.connect('files/db_new.db')
# purchares_3.to_csv('files/new_purchares.csv')
# purchares_4.to_json('files/new_data.json')
# purchares_5.to_sql('files/db_new.db', conn)

# Most important DataFrame operations
movies_data = pd.read_csv('files/movies.csv', index_col='Title')

# Output movies_data DataFrame

# print(movies_data)
# print(movies_data.head())
# print(movies_data.head(2))
# print(movies_data.tail(2))

# Getting info about your data

# print(movies_data.info())

# print(movies_data.shape)

# Handling duplicates

movies_data_2 = movies_data.append(movies_data)

# print(movies_data_2.shape)

# Drop duplicates

movies_data_3 = movies_data_2.drop_duplicates()
# print(movies_data_3.shape)

# Drop with inplace

movies_data_4 = movies_data_3.append(movies_data_3)

# print(movies_data_4.shape)

movies_data_4.drop_duplicates(inplace=True)

# print(movies_data_4.shape)

# Drop duplicates witk keep

movies_data_5 = movies_data_4.append(movies_data_4)

# print(movies_data_5.shape)

movies_data_5.drop_duplicates(inplace=True, keep=False)

# print(movies_data_5.shape)

# Column cleanup

# print(movies_data.columns)

# Rename columns

movies_data.rename(columns={
    'Rank': 'Level',
    'Ganre': 'Style'
}, inplace=True)

# print(movies_data.columns)

# Rename columns 2
movies_data.columns = ['Grade', 'Type','Mark']

# print(movies_data.columns)

# Rename use LC
movies_data.columns = [col.lower() for col in movies_data]

# print(movies_data.columns)

# Work with missing values

# print(movies_data.isnull())

# print(movies_data.isnull().sum())

# print(movies_data.sum())

# print(movies_data.dropna(), end='\n\n')

# print(movies_data.dropna(axis=1))

# Imputation

revenue = movies_data['grade']

# print(revenue)

# print(revenue.head())

revenue_mean = revenue.mean()

# print(revenue_mean)

revenue.fillna(revenue_mean, inplace=True)

# print(revenue)

# print(movies_data)

# print(movies_data.isnull().sum())

# print(movies_data.describe())

# print(movies_data['grade'].describe())

# print(movies_data['type'].describe())

# print(movies_data['type'].value_counts().head(2))

# Relationships between continuous variables

# print(movies_data.corr())

# DataFrame slicing, selecting, extracting

genre_col = movies_data['grade']

print(type(genre_col))

genre_col_2 = movies_data[['genre']]