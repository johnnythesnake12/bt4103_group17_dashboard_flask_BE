from flask import Blueprint, jsonify
from db import get_db

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/stats', methods=['GET'])
def get_stats():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, timestamp, type, location, amount FROM statistics")
            rows = cur.fetchall()
    finally:
        conn.close()
    return jsonify(rows)