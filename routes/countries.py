from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db

countries_bp = Blueprint('countries', __name__)

@countries_bp.route('/countries', methods=['GET'])
def get_screenings():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM countries")
        rows = cur.fetchall()
        return jsonify([dict(row) for row in rows]) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
