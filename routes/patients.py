from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db
patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cur.execute("SELECT * FROM Patients")
        rows = cur.fetchall()
        if not rows:
             return jsonify({"message": "No patients found"}), 404
        return jsonify([dict(row) for row in rows]) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()  
    
