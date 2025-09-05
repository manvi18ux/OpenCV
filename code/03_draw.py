# for getting blank screen
import cv2 as cv
import numpy as np
blank = np.zeros((500,500), dtype='uint8')
cv.imshow('Blank', blank)
img = cv.imread('images/flow.jpeg')
cv.imshow('Flower', img)
cv.waitKey(0)

#for getting coloured screen
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
blank[:] = 0,255,0
cv.imshow('Green',blank)
cv.waitKey(0)

# Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #thickness=cv.FILLED
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)
cv.waitKey(0)
cv.destroyAllWindows()

#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3) #or thickness=-1
cv.imshow('Circle', blank)
cv.waitKey(0)

#Draw a line
cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,255,255), thickness=3) #or thickness=-1
cv.imshow('Line',blank)
cv.waitKey(0)

#Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)
