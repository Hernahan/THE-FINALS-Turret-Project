#pyhton library that allows for better control of arrays/math stuff
import numpy as np

import cv2


#capture video and assign it to variable to use later
cap = cv2.VideoCapture(0)



#while capturing video...
while cap.isOpened():
    #ret - check if proper return
    #frame - name of variable assigning to image
    #cap.read() - captured current frame of video and assigns it to frame
    ret, frame = cap.read()
    cv2.imshow('test',frame)
    
    #if q pressed, end video prematurely
    if cv2.waitKey(1) == ord('q'):
        break

#end video
cap.release()
cv2.destroyAllWindows()
