# === Backend: app.py ===

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
import mysql.connector

app = Flask(__name__)
socketio = SocketIO(app)

# Store connected users by session ID
users = {}

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hello5@123",
    database="chatapp"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
)
''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    email = data['email']
    phone = data['phone']

    # Save to MySQL
    cursor.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    conn.commit()

    return jsonify({'status': 'success'})

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid)
    message = data['message']
    print(f"Message received from {username}: {message}")
    send({'user': username, 'message': message}, broadcast=True)

@socketio.on('set_username')
def set_username(username):
    users[request.sid] = username

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
