import datetime
import os
import ftplib
import time
from threading import Thread

filename = ""
session = ftplib.FTP('10.0.0.32','shlomi','123')
os.system("cd /home/pi/Desktop/")


def record():
    global filename
    print("\nRecording...\n")
    nowstr = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    filename = nowstr + ".avi"
    os.system("streamer -f rgb24 -r 4 -t 00:00:05 -o /home/pi/Desktop/vid.avi")
    print("\nRecording success\n")
    return

def upload():
    global filename
    print("\nUploading...\n")
    file = open("/home/pi/Desktop/vid.avi",'rb')

    session.storbinary('STOR ' + filename, file)     # send the file
    file.close()
    print("\nUploading success\n")
    return

record()
upload()

session.quit()
