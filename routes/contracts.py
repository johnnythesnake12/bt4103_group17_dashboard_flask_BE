from flask import Blueprint, jsonify
from MySQLdb.cursors import DictCursor
from db import get_db
contracts_bp = Blueprint('contracts', __name__)

@contracts_bp.route('/contracts', methods=['GET'])
def get_contracts():
    conn = get_db()
    cur = conn.cursor(DictCursor)
    try:
        cur.execute("SELECT * FROM contracts")
        rows = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
    return jsonify(rows)
