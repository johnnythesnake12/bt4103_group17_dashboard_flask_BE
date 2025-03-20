from flask import Blueprint, jsonify
from db import get_db

providers_bp = Blueprint('providers', __name__)

@providers_bp.route('/providers', methods=['GET'])
def get_providers():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM providers")
    rows = cur.fetchall()
    cur.close()
    
    # Format response as JSON
    
    return jsonify(rows)
