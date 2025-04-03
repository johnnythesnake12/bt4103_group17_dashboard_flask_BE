from flask import Blueprint, jsonify,request
import psycopg2.extras
from db import get_db

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
            providers_list = [{"provider_name": p["provider_name"], "onboarding_stage":p["onboarding_stage"]} for p in providers_list]
        return jsonify(providers_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close() 

