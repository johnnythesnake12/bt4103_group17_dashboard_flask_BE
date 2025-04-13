
# Flask Backend for Market Sizing Dashboard

This is the backend service for a healthcare market sizing dashboard built with **Flask**, **PostgreSQL (via Supabase)**, and **Vue.js** for the frontend. It exposes API endpoints to serve provider, patient, screening, transaction, and financial projection data to the frontend.

---

## Project Structure

```
.
├── app.py                        # Main Flask entrypoint
├── config.py                    # Config file (legacy/unused now)
├── db.py                        # Handles PostgreSQL DB connection using psycopg2
├── /routes                      # Contains all route Blueprints
│   ├── providers.py
│   ├── screenings.py
│   ├── contracts.py
│   ├── patients.py
│   ├── transactions.py
│   ├── countries.py
│   └── costing_projections.py
├── .env                         # Environment variables for DB connection
├── requirements.txt             # Python dependencies
└── postgres_db_initialization.sql # Schema initialization script for Supabase
```

---

## Live Deployment

- **Backend**: https://bt4103-group17-dashboard-flask-be.onrender.com (Render)
- **Frontend**: Vue.js app (fetches data from this Flask backend)

---

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL (via Supabase)
- **ORM**: Raw SQL using `psycopg2` for control and performance
- **Frontend**: Vue 3 (separate repo)
- **Deployment**: Render (Flask as a web service)

---

## API Endpoints

| Endpoint                 | Method | Description                             |
|--------------------------|--------|-----------------------------------------|
| `/providers`            | GET    | Get all healthcare providers            |
| `/screenings`           | GET    | Get all patient screening records       |
| `/contracts`            | GET    | Get all contract details                |
| `/patients`             | GET    | Get all patients                        |
| `/transactions`         | GET    | Get all transactions                    |
| `/countries`            | GET    | Get country-level data (e.g., population, revenue) |
| `/costing_projections`  | GET    | Get calculated cost/profit projections  |

> All responses are returned as JSON.

---

## Environment Variables

Create a `.env` file in your backend root:

```
DB_HOST=your-supabase-db-host.supabase.co
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_secure_password
DB_PORT=5432
```

These are used in `db.py` to initialize a connection with Supabase PostgreSQL.

---

## Running Locally

1. Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your `.env` file with your Supabase credentials

3. Run the Flask development server:

```bash
python app.py
```

> Flask runs on `http://localhost:5000` by default.

---

## Deploying on Render

1. Go to [Render](https://render.com)
2. Create a **new Web Service**
3. Configure:
   - **Environment**: Python 3.x
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Add your `.env` variables in Render's environment settings
5. Deploy!

---

## Notes

- Database connections are managed using Flask’s `g` context.
- All routes are modular and registered in `app.py` via Blueprints.
- Current deployment of the Flask application is already up and running on the free tier of Render, which may cause some delays in fetching of data to the front end webpage as the instance spins down after 50s of inactivity
---
