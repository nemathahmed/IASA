import face_recognition
from sklearn import svm
import os
import pickle
import cv2
import time
from gtts import gTTS 
import pydub
from pydub import AudioSegment
from pydub.playback import play

filename = 'finalized_model.sav'
clf = pickle.load(open(filename, 'rb'))
# Find all the faces in the test image using the default HOG-based model

language = 'en'


def show_webcam(mirror=False):
    #test_image = face_recognition.load_image_file('test_image.jpg')

    cam = cv2.VideoCapture(0)
    while True:
        #for i in range(200):
        #    ret, img=cam.read()
        #    cv2.imshow('im',img)
        #    if cv2.waitKey(1) == 27: 
        #        break
        name=""
        ret, img=cam.read()
        img=img
        face_locations = face_recognition.face_locations(img)
        ace_locations = face_recognition.face_locations(img)
        no = len(face_locations)
        print("Found:")
        print("Number of faces detected: ", no)
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(img)[i]
            name =clf.predict([test_image_enc])
            Name='Hey,'+str(name)+ ' is passing by'
            myobj = gTTS(text=Name, lang=language, slow=False) 
            myobj.save('myjarvissound.mp3')
            song = AudioSegment.from_mp3("myjarvissound.mp3")
            play(song)
            #time.sleep(5)
        print(name)
        #cv2.imshow('Photo Video Camera Stream', img)
        cv2.imshow('im',img)
        if cv2.waitKey(1) == 27: 
            break
    cv2.destroyAllWindows()

show_webcam()        
# Predict all the faces in the test image using the trained classifier
