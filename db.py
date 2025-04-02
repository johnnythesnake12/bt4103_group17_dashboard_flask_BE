import psycopg2
from flask import g
import os
from dotenv import load_dotenv
load_dotenv()

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", 5432),
            sslmode="require"
        )
    return g.db

def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
