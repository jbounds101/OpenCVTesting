import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

# Averaging (takes average of surrounding pixels)
average = cv.blur(img, (7, 7))
                        # kernel size (higher kernel = more blur)
cv.imshow('Average', average)

# Gaussian blur (pixels are given weight and multiplied)
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian', gaussian)

# Median blur (Averaging, except it find the median of the surrounding pixels (good for reducing noise))
median = cv.medianBlur(img, 7)
                            # don't need a tuple for this kernel (use low numbers, not usually used with high nums)
cv.imshow('Median', median)

# Bilateral blur (Blurs and retains edges)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)