from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for Postman & frontend)

# Database Config
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'retimark_db')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Test API Route
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Flask is running!"})

# Get All Statistics
@app.route('/stats', methods=['GET'])
def get_stats():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM statistics")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
