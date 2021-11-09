from enum import unique
import peewee

db = peewee.SqliteDatabase('database.db')

class User(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    name = peewee.CharField()
    login = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'users'

with db:
    db.create_tables([User])

print('Done')