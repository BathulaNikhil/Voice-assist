from flask import Flask, render_template
import cv2

app = Flask(__name__)

cap = cv2.VideoCapture(0)
is_camera_open = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_camera')
def open_camera():
    global is_camera_open
    is_camera_open = True
    return "Camera opened"

@app.route('/close_camera')
def close_camera():
    global is_camera_open
    is_camera_open = False
    return "Camera closed"

@app.route('/video_feed')
def video_feed():
    def generate():
        while is_camera_open:
            ret, frame = cap.read()
            if not ret:
                break
            _, jpeg = cv2.imencode('.jpg', frame)
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

    return app.response_class(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
