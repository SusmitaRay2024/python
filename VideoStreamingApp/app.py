from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import base64
import time
import eventlet

eventlet.monkey_patch()  # Required for async SocketIO with eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def stream_video():
    while True:
        success, frame = camera.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        socketio.emit('video_frame', {'image': jpg_as_text})
        socketio.sleep(0.03)  # ~30 FPS

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    socketio.start_background_task(stream_video)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
