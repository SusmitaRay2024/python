from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

# Store connected users by session ID
users = {}

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Handle messages sent from the client
@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid)  # Get the username based on session ID
    message = data['message']
    print(f"Message received from {username}: {message}")
    send({'user': username, 'message': message}, broadcast=True)  # Broadcast message to all clients

# Handle new user joining (setting username)
@socketio.on('set_username')
def set_username(username):
    users[request.sid] = username  # Associate user name with the session ID

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
