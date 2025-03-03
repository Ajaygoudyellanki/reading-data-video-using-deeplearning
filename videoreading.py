import numpy as np
import matplotlib.pyplot as plt
import cv2
import datetime
cap=cv2.VideoCapture(r'C:\Users\MOUNIKA\PycharmProjects\opencv\WIN_20241115_18_05_28_Pro.mp4')
count=0
while True:
    status,pixels=cap.read()
    if status==True:
        count=count+1
        dt=datetime.datetime.now()
        text_image=dt.strftime("%y-%m-%d %H:%M:%S")
        font_style=cv2.FONT_HERSHEY_PLAIN
        position=(50, 50)
        font_scale=1
        color=(255,255,255)
        thickness=2
        pixels=cv2.putText(pixels,text_image,position,font_style,font_scale,color,thickness)
        cv2.imshow('Frames',pixels)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break
print(count)
cap.release()
cv2.destroyAllWindows()

