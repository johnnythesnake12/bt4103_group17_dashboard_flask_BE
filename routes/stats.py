from flask import Blueprint, jsonify
from db import mysql

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/stats', methods=['GET'])
def get_stats():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, timestamp, type, location, amount FROM statistics")
    rows = cur.fetchall()
    cur.close()
    
    # Format response as JSON
    results = [
        {"id": row[0], "timestamp": row[1], "type": row[2], "location": row[3], "amount": row[4]}
        for row in rows
    ]
    
    return jsonify(results)
