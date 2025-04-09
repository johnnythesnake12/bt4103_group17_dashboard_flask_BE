from flask import Blueprint, jsonify
import psycopg2.extras
from db import get_db

screenings_bp = Blueprint('screenings', __name__)

@screenings_bp.route('/screenings', methods=['GET'])
def get_screenings():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM Screenings")
        rows = cur.fetchall()
        return jsonify([dict(row) for row in rows]) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 

@screenings_bp.route('/screenings/total_patients_screened', methods=['GET'])
def get_unique_patient_count():
    conn = get_db()
    cur = conn.cursor()
    try:
        query = "SELECT COUNT(DISTINCT patient_id) FROM Screenings"
        cur.execute(query)
        count = cur.fetchone()[0]
        return jsonify({"unique_patient_count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
    
