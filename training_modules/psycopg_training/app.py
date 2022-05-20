import psycopg2
conn = psycopg2.connect(dbname='blog', user='app', password='thisispassword')
cursor = conn.cursor()

def command(query):
    cursor.execute(query)
    if "SELECT" in query:
        return cursor.fetchall()
    return []

def print_results(list_):
    if list_:
        for i in list_:
            print(i)
    else:
        print(None)

def query_to_db(query):
    print_results(command(query))

if __name__ == "__main__":
    queries = [
        "SELECT * FROM users;",
        "SELECT u.name, count(c) from users u left join comments c on u.id=c.author group by u.name;",
        "SELECT p.title FROM likes l inner join post p on l.post=p.id;",
        "SELECT count(users.name) FROM users;",
        "SELECT p.title FROM post p;",
        f"INSERT INTO users(name, password, age, rate) values ('{input()}','{input()}', {input()}, {input()});"
    ]
    query_to_db(queries[-1])
    query_to_db(queries[0])
    conn.commit()
    conn.close()