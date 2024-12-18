from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import re
from datetime import datetime, timedelta

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "hip-mysql-iccw-hip.j.aivencloud.com",
    "user": "avnadmin",
    "password": "AVNS_aPCpCSKO_x8aBGEKcNq",
    "database": "defaultdb",
    "port": 25381,
    "ssl_ca": "ca.pem"  # Path to your CA certificate
}


def home():
    return "Flask app is running! Use /users endpoint."
# Function to connect to the database
def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connection to MySQL database was successful!")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Function to create the table if it doesn't exist
def create_table():
    try:
        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS test_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(35) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age INT NOT NULL CHECK (age BETWEEN 10 AND 100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'test_table' is ready.")
    except Error as e:
        print(f"Error while creating table: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Route to add a user
@app.route('/users', methods=['GET'])
def add_user():
    # Extract parameters
    name = request.args.get('name')
    email = request.args.get('email')
    age = request.args.get('age')

    # Validate 'name'
    if not name or len(name) > 35:
        return jsonify({"error": "'name' must not be empty and should have at most 35 characters"}), 400

    # Validate 'email'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in|org|net|edu)$'
    if not email or not re.match(email_pattern, email):
        return jsonify({"error": "'email' must be a valid email address ending in .com, .in, .org, etc."}), 400

    # Validate 'age'
    try:
        age = int(age)
        if age < 10 or age > 100:
            return jsonify({"error": "'age' must be between 10 and 100"}), 400
    except ValueError:
        return jsonify({"error": "'age' must be an integer"}), 400

    conn = None
    cursor = None
    # Insert into database
    try:
        conn = connect_to_db()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        sql = "INSERT INTO test_table (name, email, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, age))
        conn.commit()
        return jsonify({"message": "User added successfully", "id": cursor.lastrowid})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Route to fetch all records
@app.route('/users/all', methods=['GET'])
def get_all_users():
    conn = None
    cursor = None
    try:
        conn = connect_to_db()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM test_table ORDER BY created_at DESC")
        records = cursor.fetchall()
        return jsonify(records)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Route to fetch weekly records
@app.route('/users/weekly', methods=['GET'])
def get_weekly_users():
    conn = None
    cursor = None
    try:
        conn = connect_to_db()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)
        one_week_ago = datetime.now() - timedelta(days=7)
        cursor.execute("SELECT * FROM test_table WHERE created_at >= %s ORDER BY created_at DESC", (one_week_ago,))
        records = cursor.fetchall()
        return jsonify(records)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Route to fetch monthly records
@app.route('/users/monthly', methods=['GET'])
def get_monthly_users():
    conn = None
    cursor = None
    try:
        conn = connect_to_db()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)
        one_month_ago = datetime.now() - timedelta(days=30)
        cursor.execute("SELECT * FROM test_table WHERE created_at >= %s ORDER BY created_at DESC", (one_month_ago,))
        records = cursor.fetchall()
        return jsonify(records)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# Create the table before starting the Flask app
create_table()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
