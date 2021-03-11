import lab1 
from peewee import *
import os

db = 'test.db'

def test_db():
    assert os.path.exists(db) == True
    
def test_col():
    assert( 'SELECT "t1"."id", "t1"."name", "t1"."city", "t1"."address" FROM "clients" AS "t1"' == str(lab1.Clients.select()) 
    and 'SELECT "t1"."id", "t1"."client_id", "t1"."date", "t1"."amount", "t1"."description" FROM "orders" AS "t1"' == str(lab1.Orders.select()) )

def test_count():
    assert lab1.Clients.select().count() >= 10 and lab1.Orders.select().count() >= 10
    