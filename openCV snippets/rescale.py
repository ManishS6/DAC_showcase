import cv2 as cv

img = cv.imread('Photos/IMG_8008.JPG')
cv.imshow('Cat',img)

# This works for image, video or live video
def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimesions = (width,height)

    return cv.resize(frame,dimesions, interpolation=cv.INTER_AREA)

# This works only with live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

# Reading videos
capture = cv.VideoCapture('Photos/IMG_8010.MOV')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    # If the video run out of frames then opencv will raise an -215:Assertion failed error
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)