from flask import jsonify, abort
from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "admin123",  # Replace with your MySQL password
    "database": "users_db"
}

# Establish Database Connection


def get_db_connection():
    return mysql.connector.connect(**db_config)

# Route 1: /hello


@app.route('/hello')
def hello_world():
    return "Hello World!"

# Route 2: /users (Display all users in an HTML table)


@app.route('/users')
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users)

# Route 3: /new_user (Render a form to add a new user)


@app.route('/new_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        conn.commit()
        cursor.close()
        conn.close()
        return "User added successfully!"
    return render_template('new_user.html')

# Route 4: /users/<id> (Get user details by ID)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query to fetch the user by ID
        cursor.execute("SELECT * FROM Users WHERE ID = %s", (user_id,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        # If no user is found, raise a 404 error
        if not user:
            abort(404, description=f"User with ID {user_id} not found")

        # Return user details in JSON format
        return jsonify(user)

    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({"error": str(e)}), 500
