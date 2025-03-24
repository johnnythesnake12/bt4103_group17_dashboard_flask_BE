from flask import Flask, jsonify, request
import pymysql 
from flask_cors import CORS
from config import Config
from dotenv import load_dotenv
from db import get_db


load_dotenv()

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)




@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Flask is running!"})

# Example route: Get All Statistics
@app.route('/stats', methods=['GET'])
def get_stats():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM statistics")
            rows = cur.fetchall()
    finally:
        conn.close()
    return jsonify(rows)

# Route: Get All rows from Patients table
@app.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PATIENTS")
            rows = cur.fetchall()
    finally:
        conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
