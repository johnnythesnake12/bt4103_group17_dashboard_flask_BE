from flask import Blueprint, jsonify
from db import get_db

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['GET'])

def get_patients():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PATIENTS")
            rows = cur.fetchall()
    finally:
        conn.close()
    return jsonify(rows)