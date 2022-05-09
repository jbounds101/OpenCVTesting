import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

# Convert an image to grayscale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# from  color conversion

# Blur, remove extra noise
img = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# from  blur amt    border?

# Edge cascade (find edges in image)
img = cv.Canny(img, 125, 175)
# threshold values

# Dilate an img using structuring element
dilated = cv.dilate(img, (10, 10), iterations=1)

# Eroding (using dilated image)
eroded = cv.erode(dilated, (3, 3), iterations=1)

# Resize
img = cv.resize(eroded, (500, 500))  # ignores aspect ratio
img = cv.resize(eroded, (500, 500), interpolation=cv.INTER_AREA)  # for downsize
# use cv.INTER_CUBIC or cv.INTER_LINEAR for upscale

# Cropping
cropped = img[50:200, 100:400]
            # height   width

cv.imshow('Cat', cropped)
cv.waitKey(0)
