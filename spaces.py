import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR won't display properly in other packages

# BGR to RGB (normal)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.waitKey(0)