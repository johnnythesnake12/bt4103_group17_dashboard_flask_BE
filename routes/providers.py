from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db


providers_bp = Blueprint('providers', __name__)

@providers_bp.route('/providers', methods=['GET'])
def get_providers():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM Providers")
        rows = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
    return jsonify([dict(row) for row in rows])
