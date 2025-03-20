from flask import Blueprint, jsonify
from db import mysql

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/stats', methods=['GET'])
def get_stats():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM statistics")
    rows = cur.fetchall()
    cur.close()
    
    # Format response as JSON
    
    return jsonify(rows)
