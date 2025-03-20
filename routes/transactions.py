from flask import Blueprint, jsonify
from MySQLdb.cursors import DictCursor
from db import get_db
transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    conn = get_db()
    cur = conn.cursor(DictCursor)
    try:
        cur.execute("SELECT * FROM transactions")
        rows = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()  # Always close the cursor
    
    return jsonify(rows)
