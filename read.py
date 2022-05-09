import cv2 as cv


# Resize method
def rescaleFrame(frame, scale=0.75):
    # frame.shape[0] = height
    # frame.shape[1] = width
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)  # create a tuple

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


'''def changeVideoResolution(width, height):
    capture.set(3, width)
    capture.set(4, height)'''

# Reading photos
'''img = cv.imread('Resources/Photos/cat.jpg')  # open a photo file
cv.imshow('Cat', img)  # open a window with 'Cat' at the top and the img from earlier
img = rescaleFrame(img, scale=0.5)
cv.waitKey(0)  # waits for keyboard input'''

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')  # Can also use non-path arguments (replaced with int) to get
# live video feed, such as a webcam

while True:
    isTrue, frame = capture.read()  # isTrue is if the frame was captured correctly, frame is the frame of the video
    # captured, you have to read frame by frame for a video

    if not isTrue:  # break from reading after running out of frames
        break

    cv.imshow('Video', frame)  # will give a -215 error if the frame couldn't be found, this will happen if the
    # video runs out of frames

    if cv.waitKey(20) & 0xFF == ord('d'):  # break on 'd' key
        break

capture.release()  # video captures must be released (closed) after use
cv.destroyAllWindows()  # closes all the windows ope
