import psycopg2
conn = psycopg2.connect(dbname='blog', user='app', password='thisispassword')
cursor = conn.cursor()

def command(query):
    cursor.execute(query)
    return cursor.fetchall()

def print_results(list_):
    if list_:
        for i in list_:
            print(i)
    else:
        print(None)

def query_to_db(query):
    print_results(command(query))

if __name__ == "__main__":
    # query_to_db("SELECT * FROM users;")
    query_to_db("SELECT u.name, count(c) from users u left join comments c on u.id=c.author group by u.name;")