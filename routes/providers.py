from flask import Blueprint, jsonify
from db import get_db

providers_bp = Blueprint('providers', __name__)

@providers_bp.route('/providers', methods=['GET'])
def get_providers():
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM providers")
        rows = cur.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()  # Always close the cursor
    
    return jsonify(rows)
