from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config
from db import init_db, mysql
from dotenv import load_dotenv
from routes.stats import stats_bp
from routes.providers import providers_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for Postman & frontend)
app.config.from_object(Config) 
init_db(app)

app.register_blueprint(stats_bp)
app.register_blueprint(providers_bp)
if __name__ == '__main__':
    app.run(debug=True)
