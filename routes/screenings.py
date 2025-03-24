from flask import Blueprint, jsonify
from pymysql.cursors import DictCursor
from db import get_db

screenings_bp = Blueprint('screenings', __name__)

@screenings_bp.route('/screenings', methods=['GET'])
def get_screenings():
    conn = get_db()
    cur = conn.cursor(DictCursor)
    try:
        cur.execute("SELECT * FROM screenings")
        rows = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
    return jsonify(rows)
