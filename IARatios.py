import numpy as np
import cv2
import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Bootup.mp3")
pygame.mixer.music.play(1,0.0)
while(True):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        print("No frame")
        pygame.mixer.music.load("discharged-battery-151926.mp3")
        pygame.mixer.music.play(1,0)
        time.sleep(15)
    else:
        break
pygame.mixer.music.load("Camera_detected.mp3")
pygame.mixer.music.play(1,0)
#cap = cv2.VideoCapture("vid_04_003.avi")
pygame.mixer.init()
pygame.mixer.music.load("cute-level-up-3-189853.mp3")
pygame.mixer.music.play(-1,0.0)
square = 0 #0 equals small square, 1  = Large square
threshold_store = [155000, 4900000]
pixeldiffthreshold = [100,100000]
framesinarow = 0
bool1=True
LastDetection = 0 # 0 = Green, 1 = Gray, 2 = Half-Covered, 3 = speed limit sign
LastSignal = -1
while(bool1):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        bool1 = False
        break
    totalpixvalue = [0,0,0]
    # Big Square
    numpixeldiff = 0
    if(square == 1):
        lastpixel = frame[220][180][0]
        for y in range(220, 420):
            for x in range(180, 400):
                totalpixvalue+=frame[y][x]
                frameyxR = frame[y][x][0]
                if((lastpixel-frame[y][x][0]>30)|(frame[y][x][0]-lastpixel>30)):
                    numpixeldiff+=1
                lastpixel = frame[y][x][0]
    else:# Little Square
        # print("Fuck")
        lastpixel = frame[288][270][0]
        for y in range(288, 328):
            for x in range(270,310):
                if((lastpixel>30+frame[y][x][0])|(frame[y][x][0]>lastpixel+30)):
                    numpixeldiff+=1
                lastpixel = frame[y][x][0]
                totalpixvalue+=frame[y][x]
    # print(numpixeldiff)
    if(numpixeldiff>pixeldiffthreshold[square]):
        if(LastDetection != 3):
            LastDetection = 3
            # print("Gray")
            # print(totalpixvalue)
            framesinarow = 0
        else:
            framesinarow +=1
            if (framesinarow==2):
                if(LastSignal!=LastDetection):
                    print("Speedlimit")
                    LastSignal = 3
        
    elif(totalpixvalue[0]<threshold_store[square]):
        if(LastDetection!=2):
            LastDetection =2
            LastSignal = 2
            print("Half-Covered")
            # print(totalpixvalue)
    else:
        if(totalpixvalue[0]>totalpixvalue[1]):
            if(LastDetection != 1):
                LastDetection = 1
                # print("Gray")
                # print(totalpixvalue)
                framesinarow = 0
            else:
                framesinarow +=1
                if (framesinarow==2):
                    if(LastSignal!=LastDetection):
                        print("Gray")
                        #pygame.mixer.music.set_volume(100)
                        LastSignal = 1
                    # print(totalpixvalue)
            # print(str(LastDetection) + " : " +str(totalpixvalue))
        else:
            
            if(LastDetection != 0):
                LastDetection = 0
                framesinarow = 0
                # print("Green")
                # print(totalpixvalue)
            else:
                framesinarow +=1
                if (framesinarow==2):
                    if(LastSignal!=LastDetection):
                        print("Green")
                        #pygame.mixer.music.set_volume(0)
                        LastSignal = 0
                    # print(totalpixvalue)
           # print(str(LastDetection) + " : " +str(totalpixvalue))
    cv2.imshow('frame', frame)
    if(cv2.waitKey(1) ==ord('q')):
        pygame.mixer.music.stop()
        bool1 = False
        break
        #if (cv2.waitKey(1) == ord('q'))|(cv2.waitKey(0)==ord('c')):
        # print("Quitting")
        # bool1 = False
        # break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

