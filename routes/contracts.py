from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db
contracts_bp = Blueprint('contracts', __name__)

@contracts_bp.route('/contracts', methods=['GET'])
def get_contracts():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM Contracts")
        rows = cur.fetchall()
        return jsonify([dict(row) for row in rows]) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
