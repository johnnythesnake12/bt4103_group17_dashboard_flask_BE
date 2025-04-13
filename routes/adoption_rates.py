from flask import Blueprint, jsonify
from collections import defaultdict

from db import get_db
adoption_rates_bp = Blueprint('adoption_rates', __name__)


@adoption_rates_bp.route("/api/adoption-rates", methods=["GET"])
def get_adoption_rates():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT country,
               TO_CHAR(DATE_TRUNC('month', used_at), 'YYYY-MM') AS month,
               COUNT(DISTINCT user_id) AS new_active_users
        FROM screenings
        JOIN patients ON patients.patient_id = screenings.user_id
        GROUP BY country, month
        ORDER BY month;
    """)
    data = cur.fetchall()
    rows = cur.fetchall()

    data_by_country = defaultdict(dict)
    all_months = set()

    # Fill data into a country => month => value structure
    for country, month, value in rows:
        data_by_country[country][month] = value
        all_months.add(month)

    # Sort months for consistent x-axis
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