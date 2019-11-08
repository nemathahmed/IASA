import pydub
pydub.AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
from pydub import AudioSegment
from pydub.playback import play
import os
import time
import winsound
from threading import Thread                                                                  
from multiprocessing import Pool   
processes = ('arc.py')
import subprocess
def getangles():
    print('Enter <Mode> <Angles>')
    arr=[str(x) for x in input().split()]
    return arr[0],arr[1:len(arr)]
def combine(arr):
    print(arr,'yes')
    print("E:/Computer Vision/SoundLocalize/FINAL EDITS/"+"BASE.mp3")
    soundbase=AudioSegment.from_mp3("E:/Computer Vision/SoundLocalize/FINAL EDITS/"+arr[0]+" DEG.mp3")

    for i in range(0,len(arr)):
        print("E:/Computer Vision/SoundLocalize/FINAL EDITS/"+arr[i]+" DEG.mp3")
        sound1 = AudioSegment.from_mp3("E:/Computer Vision/SoundLocalize/FINAL EDITS/"+arr[i]+" DEG.mp3")
        soundbase = soundbase.overlay(sound1)
    return soundbase
def combine_1(arr):
    print(arr,'yes')
    print("E:/Computer Vision/SoundLocalize/FINAL EDITS 130 HZ/BASE.mp3")
    soundbase=AudioSegment.from_mp3("E:/Computer Vision/SoundLocalize/FINAL EDITS 130 HZ/BASE.mp3")

    for i in range(0,len(arr)):
        print("E:/Computer Vision/SoundLocalize/FINAL EDITS 130 HZ/"+arr[i]+" DEG.mp3")
        sound1 = AudioSegment.from_mp3("E:/Computer Vision/SoundLocalize/FINAL EDITS 130 HZ/"+arr[i]+" DEG.mp3")
        soundbase = soundbase.overlay(sound1)
    return soundbase
def export(soundfinal):
    soundfinal.export("finalmusic.wav", format='wav')

mode,angle_arr=getangles()
print(mode,angle_arr)
if int(mode)==0:
    final=combine(angle_arr)
    export(final)
elif int(mode)==1:
    final=combine_1(angle_arr)
    export(final)
arr_int=[]
for i in range(len(angle_arr)):
    arr_int.append(int(angle_arr[i]))
def play_sound():
    winsound.PlaySound("finalmusic.wav", winsound.SND_ALIAS)
for i in range(1):
    thread = Thread(target=play_sound)
    thread.start()
    import turtle
    import numpy as np
    import time
    radius=300
    angle=-70
    turtle.speed('fastest')
    turtle.setpos(-285,93)
    for i in range(140):
        #print(int(angle))
        theta=(angle*np.pi)/180
        if int(angle) in arr_int:
            print('Angle ',angle,'Processed')
            turtle.write(int(angle))
        turtle.setpos(300*np.sin(theta),300*np.cos(theta))
        time.sleep(0.06550)
    
        angle=angle+1




#song = AudioSegment.from_wav("finalmusic.wav")
#play(song)

                                                                                



