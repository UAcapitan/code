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
    # db.create_tables([User])
    # user_1 = User(name='Ed', login='EdMix', password='edmix22').save()
    # user_2 = User(name='Max', login='Maximum', password='max873629').save()
    # user_3 = User(name='Ken', login='Teacher', password='teacher20').save()
    all_users = User.select()

for i in all_users:
    print(i.id, i.name, i.login, i.password)

print('Done')