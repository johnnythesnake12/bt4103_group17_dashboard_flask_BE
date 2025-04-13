from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db

costing_projections_bp = Blueprint('costing_projections', __name__)

@costing_projections_bp.route('/costing_projections', methods=['GET'])
def get_costing_projections():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM costing_projections")
        rows = cur.fetchall()
        return jsonify([dict(row) for row in rows]) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 
    
