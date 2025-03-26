from flask import Blueprint, jsonify
from pymysql.cursors import DictCursor
from db import get_db
patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db()
    cur = conn.cursor(DictCursor)

    try:
        cur.execute("SELECT * FROM Patients")
        rows = cur.fetchall()
        if not rows:
             return jsonify({"message": "No patients found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()  
    
    return jsonify(rows)
