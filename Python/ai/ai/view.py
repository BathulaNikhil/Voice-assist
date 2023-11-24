from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip
import cv2
import threading
import time
import sys

cap = cv2.VideoCapture(0)
is_camera_open = False
global_frame = None

def video_feed():
    global is_camera_open, cap, global_frame
    while is_camera_open:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        global_frame = jpeg.tobytes()
        time.sleep(0.1)

@gzip.gzip_page
def webcam(request):
    return render(request, 'index.html')

def open_camera(request):
    global is_camera_open
    is_camera_open = True
    threading.Thread(target=video_feed).start()
    return HttpResponse("Camera opened")

def close_camera(request):
    global is_camera_open
    is_camera_open = False
    return HttpResponse("Camera closed")

def get_frame(request):
    global global_frame
    return HttpResponse(global_frame, content_type='image/jpeg')
