import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# AND (intersection)
bitAnd = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitAnd)

# OR (combination)
bitOr = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitOr)

# XOR (non intersecting regions)
bitXor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitXor)

# NOT
bitNot = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitNot)

cv.waitKey(0)