import sys
import argparse
from peewee import *
import random
from datetime import date
from prettytable import PrettyTable
x = PrettyTable()
 
def gen_db():
    if Clients.table_exists()==False and Orders.table_exists()==False :
            db.create_tables([Clients, Orders])
    else:
        db.drop_tables([Clients, Orders])
        db.create_tables([Clients, Orders])
    return 0
        

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name', nargs='?')
    parser.add_argument ('nametab', nargs='?')
    return parser
 
db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db

class Clients(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

class Orders(BaseModel):
    client = ForeignKeyField(Clients)
    date = DateField()
    amount = CharField()
    description = CharField()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    cursor = db.cursor()

    if namespace.name =='init':
        # if Clients.table_exists()==False and Orders.table_exists()==False :
        #     db.create_tables([Clients, Orders])
        # else:
        #     db.drop_tables([Clients, Orders])
        #     db.create_tables([Clients, Orders])
        gen_db()
    elif namespace.name == 'fill':
        d = ['Space-X','Ultra','Zabava','1c']
        d1 = ['Surgut','New-York','London','Berlin']
        d2 = ['Wall street','Dzershinskogo','Lenina','Baker street']
        d3 = ['good','bad','low','fast']
        for i in range(1, 11):
            start_date = date.today().replace(day=1, month=1).toordinal()
            end_date = date.today().toordinal()
            random_day = date.fromordinal(random.randint(start_date, end_date))
            Clients.create(name=random.choice(d), city=random.choice(d1), address=random.choice(d2))
            Orders.create(client=random.choice(d), date=random_day, amount=str(random.randint(1, 100)),description = random.choice(d3))
    elif namespace.name =='show':
        if namespace.nametab =='Clients':
            q = Clients.select(Clients.name, Clients.city, Clients.address)
            x.field_names = ["name", "city", "address"]
            for Clients in q:
                x.add_row([Clients.name, Clients.city, Clients.address])
            print(x)
        elif namespace.nametab =='Orders':
            q = Orders.select(Orders.client_id, Orders.date, Orders.amount, Orders.description)
            x.field_names = ["client", "date", "amount", "description"]
            for Orders in q:
                x.add_row([Orders.client_id, Orders.date, Orders.amount, Orders.description])
            print(x)
        else:
            print('This table no exist')
    else:
        print('Команды в программе: ')
        print('1) запуск с параметром init создаст бд')
        print('2) запуск с параметром fill заполнит бд рандомными данными')
        print('3) запуск с параметром show и название таблицы выведет данные по данной таблице')
        sys.exit
        
    db.close()