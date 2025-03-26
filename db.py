import pymysql
from flask import g

def get_db():
    if 'db' not in g:
        # Configure the connection to your Cloud SQL MySQL database
        g.db = pymysql.connect(
            host="34.162.199.100",  #  Cloud SQL Public IP
            user="retimark",         #  MySQL user
            password="password",     #  MySQL password
            database="data-storage", #  database name
            port=3306,               

        )
    return g.db

def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
