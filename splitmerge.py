import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)  # splits into color channels (as grayscale, light parts = high density of that color)

blue = cv.merge([b, blank, blank])  # will make it actually blue

cv.imshow('Real blue', blue)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

merged = cv.merge([b, g, r])
cv.imshow('Merge', merged)

cv.waitKey(0)