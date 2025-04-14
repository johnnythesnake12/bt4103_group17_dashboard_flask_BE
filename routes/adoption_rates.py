from flask import Blueprint, jsonify
from collections import defaultdict

from db import get_db
adoption_rates_bp = Blueprint('adoption_rates', __name__)


@adoption_rates_bp.route("/adoption-rates", methods=["GET"])
def get_adoption_rates():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            pr.country,
            TO_CHAR(DATE_TRUNC('month', s.screening_date), 'YYYY-MM') AS month,
            COUNT(DISTINCT s.patient_id) AS new_active_users,
            total.total_users
        FROM screenings s
        JOIN providers pr ON pr.provider_id = s.provider_id
        JOIN (
        SELECT 
            pr.country,
            COUNT(*) AS total_users
            FROM patients pa
            JOIN screenings s2 ON s2.patient_id = pa.patient_id
            JOIN providers pr ON pr.provider_id = s2.provider_id
            GROUP BY pr.country
        ) AS total ON total.country = pr.country
        GROUP BY pr.country, month, total.total_users
        ORDER BY month;

    """)
    data = cur.fetchall()
    data_by_country = defaultdict(dict)
    all_months = set()

    for country, month, value, total_users in data:
        adoption_rate = round((value / total_users) * 100, 2)
        data_by_country[country][month] = adoption_rate
        all_months.add(month)

    sorted_months = sorted(all_months)

    datasets = []
    for country, month_data in data_by_country.items():
        datasets.append({
            "label": country,
            "data": [month_data.get(month, 0) for month in sorted_months]
        })

    result = {
        "labels": sorted_months,
        "datasets": datasets
    }


    return jsonify(result)