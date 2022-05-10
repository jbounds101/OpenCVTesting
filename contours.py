import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(img, 125, 175)  # get edges

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
                                    # edge img | mode to find contours | way to approximate contours

# contours is a list of the locations of all contours found
# hierarchies is too complex for this


cv.imshow('Display', img)

cv.waitKey(0)