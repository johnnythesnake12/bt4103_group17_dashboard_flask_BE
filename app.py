from flask import Flask, jsonify, request
import pymysql 
from flask_cors import CORS
from config import Config
from db import get_db, close_db
from dotenv import load_dotenv
from routes.providers import providers_bp
from routes.screenings import screenings_bp
from routes.contracts import contracts_bp
from routes.patients import patients_bp
from routes.transactions import transactions_bp
# Load environment variables
from routes.screenings import screenings_bp
from routes.contracts import contracts_bp
from routes.patients import patients_bp
from routes.transactions import transactions_bp
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for Postman & frontend)

app.register_blueprint(providers_bp)
app.register_blueprint(screenings_bp)
app.register_blueprint(contracts_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(transactions_bp)
app.teardown_appcontext(close_db)
if __name__ == '__main__':
    app.run(debug=True)
