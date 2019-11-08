from __future__ import print_function
import darkflow

from darkflow.net.build import TFNet
import pydub
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS 
import argparse
import socket
import sys
import binascii
import struct
from collections import namedtuple
import cv2
import numpy as np
import matplotlib.pyplot as plt
options = {"model": "darkflow/cfg/yolo.cfg", 
           "load": "bin/yolo.weights", 
           "threshold": 0.1, 
           "gpu": 1.0}

tfnet = TFNet(options)
print('efjnefjen')
cap = cv2.VideoCapture('rtsp://10.250.2.76:8080/h264_ulaw.sdp')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('./sample_video/output.avi',fourcc, 20.0, (int(width), int(height)))

while(True):
    
    p=int(input())
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True:
        
        frame = np.asarray(frame)
        results = tfnet.return_predict(frame)

        arr=[]
        # Display the resulting frame
        for result in results:
            arr.append(result['label'])
        print(arr)

        for ii in range(len(arr)):
            Name=str(arr[ii])
            myobj = gTTS(text=Name, lang='en', slow=False) 
            myobj.save('myjarvissound.mp3')
            song = AudioSegment.from_mp3("myjarvissound.mp3")
            play(song)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()