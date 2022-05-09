import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # creates a blank 500x500 image (uint8 is picture dtype)

# 1. Paint image a certain color
blank[:] = 0, 255, 0   # paint all pixels green

# 2. Draw a rectangle
cv.rectangle(blank, (300, 300), (450, 490), (255, 0, 0), thickness=-1)
            # onto  start pos   end pos     color        other vars

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=-1)  # thickness -1 is filled

# 3. Draw a circle
cv.circle(blank, (250, 250), 40, (0, 170, 170), thickness=3)
        # onto    mid-point  rad   color

# 4. Draw a line
cv.line(blank, (0, 0), (400, 400), (100, 180, 290), thickness=7)

# 5. Write text
cv.putText(blank, "Wowee", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 90, 255), thickness=2)


cv.imshow('Blank', blank)

cv.waitKey(0)