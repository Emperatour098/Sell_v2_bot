import orm_sqlite  

class Pomodoro(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    task = orm_sqlite.StringField()
    interval = orm_sqlite.IntegerField()
    
db = orm_sqlite.Database('example.db')
Pomodoro.objects.backend = db