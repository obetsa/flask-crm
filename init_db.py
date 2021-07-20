import sqlite3
from datetime import datetime
from pony.orm import *

connection = sqlite3.connect('database.db')

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
DIR = 'C:\\Users\\Andrii\\Desktop\\flask-crm'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class Departments(db.Entity):
    department_id = PrimaryKey('Employees')
    department_name = Optional(str)


class Employees(db.Entity):
    employee_id = PrimaryKey('Orders')
    fio = Optional(str)
    position = Optional(int)
    department_id = Set(Departments)


class Orders(db.Entity):
    order_id = PrimaryKey(str)
    created_dt = Optional(datetime)
    updated_dt = Optional(datetime)
    order_type = Optional(str)
    description = Optional(str, nullable=True)
    status = Optional(str)
    serial_no = Optional(int)
    creator_id = Set(Employees)


db.generate_mapping(create_tables=True)
