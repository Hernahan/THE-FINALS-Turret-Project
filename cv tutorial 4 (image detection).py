import numpy as np
import cv2

#read images as grayscale [0] because most detection algorithms require grayscale

#mother image
img = cv2.imread('assets\Screenshot 2024-10-04 182015.png', 0)
#image to be detected
template = cv2.imread('assets\Screenshot 2024-10-04 182001.png',0)