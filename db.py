import pymysql
from pymysql.cursors import DictCursor
from flask import current_app

def get_db():
    connection = pymysql.connect(
        host=current_app.config["MYSQL_HOST"],
        user=current_app.config["MYSQL_USER"],
        password=current_app.config["MYSQL_PASSWORD"],
        db=current_app.config["MYSQL_DB"],
        cursorclass=DictCursor,
        autocommit=True 
    )
    return connection
