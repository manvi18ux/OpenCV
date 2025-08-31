import cv2 as cv

#image
img = cv.imread('images/flow.jpeg')

cv.imshow('flower',img)

def rescaleFrame(frame, scale=0.75):
    #this method will work for images, videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)

cv.imshow('Image', resized_image)

def changeRes(width,height):
    #will only work for live videos
    capture.set(3,width)
    capture.set(4,height)

#video
capture = cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read() #read video frame by frame, isTrue says whether the video was read or not

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #wait for 20ms before showing next frame, if 'd' is pressed, break the loop
        break

    capture.release()
    
    cv.destroyAllWindows()



cv.waitKey(0)