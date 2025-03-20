from flask import Blueprint, jsonify
from db import mysql, get_db

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/stats', methods=['GET'])
def get_stats():
    conn = get_db()  
    cur = conn.cursor()
    cur.execute("SELECT * FROM statistics")
    rows = cur.fetchall()
    cur.close()
    

    
    return jsonify(rows)
