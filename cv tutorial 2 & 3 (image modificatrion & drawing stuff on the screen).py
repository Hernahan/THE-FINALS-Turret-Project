#pyhton library that allows for better control of arrays/math stuff
import numpy as np

import cv2


#capture video and assign it to variable to use later
#(0) means your webcam
cap = cv2.VideoCapture(0)



#while capturing video...
while cap.isOpened():
    #ret - check if proper return
    #frame - name of variable assigning to image
    #cap.read() - captured current frame of video and assigns it to frame
    ret, frame = cap.read()

    
    #get width(3) and height(4)
    width = int(cap.get(3))
    height = int(cap.get(4)) 

    #draw elementary line
    #(1) on the frame
    #(2) initial starting point (0,0 is top left)
    #(3) ending point (bottom right in this case)
    #(4) line pixel thickness
    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 5)

    #draw elementary rectangle
    #(1) source image 
    #(2) center point of the rectangle
    #(3) radius height and width
    #(4) color
    #(5) line thickness [-1 to fill]
    img = cv2.rectangle(img, (100,100), (200,200), (0,0,255), 5)

    #draw elementary circle
    #(1) source image
    #(2) center position 
    #(3) radius
    #(4) color
    #(5) line thickness [-1 to fill again]
    img = cv2.circle(img, (300, 300), 60, (0, 255, 0), 5)

    cv2.imshow('test',img)

    #if q pressed, end video capture
    if cv2.waitKey(1) == ord('q'):
        break

#end video
cap.release()
cv2.destroyAllWindows()
