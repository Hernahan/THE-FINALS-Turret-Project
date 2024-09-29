import cv2

#reads image from assets folder, and -1 means load it in color (0 means grayscale, 1 means color honoring transparency)
img = cv2.imread('assets\IMG_8192.JPEG', -1)

#resize to specified resolution, oterwise it'll just load in default res
img = cv2.resize(img, (500,500))

#can also resize using function fx (horizontal) and fy (vertical)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#rotate clockwise...
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


#actually shows the image (opencv just reads it with the first command and gets it ready to be shown)
#first argument tells type of media, second argument loads the media asscoiated to that name
cv2.imshow('Image', img)


#now wait *x* ms to press key until skipping line
#0 means infinite time
cv2.waitKey(750)

#get rid of the image so it isn't taking up ram in the background
cv2.destroyAllWindows()