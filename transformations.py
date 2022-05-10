import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')


# Translation (shift up x or y)
def translate(img, x, y):
    # -x (left)
    # +x (right)
    # -y (up)
    # +y (down)
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

translated = rotate(img, 45)


# Resizing
translated = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

# Flipping
translated = cv.flip(img, 0)
# 0 = vertical
# 1 = horizontal
# -1 = both

cv.imshow('Translated', translated)

cv.waitKey(0)