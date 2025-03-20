from flask import Flask, jsonify, request
import pymysql 
from flask_cors import CORS
from config import Config
from db import init_db, mysql
from dotenv import load_dotenv
from routes.stats import stats_bp
from routes.providers import providers_bp
from routes.screenings import screenings_bp
from routes.contracts import contracts_bp
from routes.patients import patients_bp
from routes.transactions import transactions_bp
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for Postman & frontend)
app.config.from_object(Config) 
init_db(app)

app.register_blueprint(stats_bp)
app.register_blueprint(providers_bp)
app.register_blueprint(screenings_bp)
app.register_blueprint(contracts_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(transactions_bp)
if __name__ == '__main__':
    app.run(debug=True)
