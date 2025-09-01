import cv2 as cv
img = cv.imread('images/flow.jpeg')
cv.imshow('Flower',img)
 #Converting to grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)
cv.destroyAllWindows()


#Edge cascade
canny = cv.Canny(img, 125, 175) #instead of img, write blur then edges will be reduced
cv.imshow('Canny Edges', canny)
cv.waitKey(0)
cv.destroyAllWindows()

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)
cv.waitKey(0)
cv.destroyAllWindows()

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)
cv.waitKey(0)
cv.destroyAllWindows()

#Resize
resized = cv.resize(img, (500,500)) #we can use interpolations according to our need, among all three 'cubic' is the slowest but the image we get is of a much higher quality.
cv.imshow('Resized',resized)
cv.waitKey(0)
cv.destroyAllWindows()

#Cropping
cropped = img[50:200 , 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
cv.destroyAllWindows()
