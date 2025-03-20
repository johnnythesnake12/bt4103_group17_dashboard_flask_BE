import pymysql
from flask import g


def get_db():
    if 'db' not in g:
        # Configure the connection to your MySQL database
        g.db = pymysql.connect(
            host="localhost", 
            user="root",  
            password="password", 
            database="retimark_db"  
        )
    return g.db

def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
