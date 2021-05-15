import cv2 as cv
# Reading images
# img = cv.imread('Photos/EHFC5871.JPG')
# cv.imshow('Cat', img)

# Reading videos
capture = cv.VideoCapture('Photos/IMG_8010.MOV')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    # If the video run out of frames then opencv will raise an -215:Assertion failed error
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
