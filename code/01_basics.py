import cv2 as cv

#image
img = cv.imread('images/flow.jpeg')

cv.imshow('flower',img)

cv.waitKey(0)

#video
capture = cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read() #read video frame by frame, isTrue says whether the video was read or not
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'): #wait for 20ms before showing next frame, if 'd' is pressed, break the loop
        break

    capture.release()
    cv.destroyAllWindows()


