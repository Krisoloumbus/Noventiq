import os
import pyodbc
from flask import jsonify
from dotenv import load_dotenv
from pathlib import Path

# Load db.env file
env_path = Path(__file__).parent / "db.env"
load_dotenv(dotenv_path=env_path)

# Safe loading with defaults
DB_DRIVER = os.getenv('DB_DRIVER', '').strip()
DB_SERVER = os.getenv('DB_SERVER', '').strip()
DB_NAME = os.getenv('DB_NAME', '').strip()
DB_USER = os.getenv('DB_USER', '').strip()
DB_PASSWORD = os.getenv('DB_PASSWORD', '').strip()

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{{DB_DRIVER}}};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

def register_health_route(app):
    @app.route('/health')
    def health():
        conn = get_db_connection()
        if conn:
            conn.close()
            return jsonify({'status': 'healthy'}), 200
        else:
            return jsonify({'status': 'unhealthy'}), 500
