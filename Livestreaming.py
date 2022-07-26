from flask import Flask, render_template, Response
# Response to take response from cam
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


# read the camera frame
def generate_frames():
    while True:
        success, frame = camera.read()
        # camera().read returns 2 parameters, one for status(frame available or not)(i named success)  and the 2nd
        # returns the frame if it can be read from camera(i named frame)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # im importing the frame in jpg format
            frame = buffer.tobytes()  # convert the buffer back to bytes
            # if i return the frame here(ex- return frame), itll only capture n return 1 frame, so- we use yield
            # keyword with generator

            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           # contetnt-type is written when images are in bytes and being passed on post side



@app.route('/')
def index():
    return render_template('mainindex.html')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')


# myfunc() will take frame from webcam and pass the response back to index.html
# mimetype is an argument, google se chipkaya :)
# this func is defined from 7th line

if __name__ == "__main__":
    app.run(debug=True)
