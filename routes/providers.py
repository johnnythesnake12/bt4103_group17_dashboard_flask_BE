from flask import Blueprint, jsonify,request
import psycopg2.extras
from db import get_db
from collections import Counter

providers_bp = Blueprint('providers', __name__)

@providers_bp.route('/providers', methods=['GET'])
def get_providers():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT * FROM Providers")
        providers = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        providers_list = [dict(zip(column_names, p)) for p in providers]
        if request.args.get("view") == "summary":
            stage_counts = Counter([p["onboarding_stage"] for p in providers_list])
            providers_list = [{"stage": stage, "total":count} for stage,count in stage_counts.items()]
        return jsonify(providers_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 

@providers_bp.route('/providers/total_worked_with', methods=['GET'])
def get_total_providers_worked_with():
    conn = get_db()
    cur = conn.cursor()
    try:
        query = """
            SELECT COUNT(*) 
            FROM Providers 
            WHERE onboarding_stage NOT IN ('not_contacted', 'contacted')
        """
        cur.execute(query)
        total = cur.fetchone()[0]
        return jsonify({"total_providers_worked_with": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
