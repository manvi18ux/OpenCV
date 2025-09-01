#blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
blank[:] = 0,255,0
cv.imshow('Green', blank)
=> (500,500,3) → 3 channels (BGR) → supports colors.

blank[:] = 0,255,0 fills entire canvas with Green.

"Green" window shows the solid-colored image.
-----------------------------------------------------------------------------------------------------
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) 
cv.imshow('Rectangle', blank)
=> Draws a green rectangle.

Start point: (0,0) → top-left.

End point: (250,250) → bottom-right.

Thickness: 2 → border only.

If thickness=-1 or cv.FILLED, rectangle is filled.

blank.shape[1] → width, blank.shape[0] → height.
-----------------------------------------------------------------------------------------------------------

#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

=> Center: (width//2, height//2) → middle of canvas.

Radius: 40.

Color: (0,0,255) → red.

Thickness: 3 (border) or -1 for filled.
---------------------------------------------------------------------------------------------------------
#cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (400,400), (255,255,255), thickness=3)
=>This will draw a white line from canvas center to (400,400).
---------------------------------------------------------------------------------------------------------
#cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
=> Text: "Hello".

Start position: (255,255) → where text starts (x,y).

Font: cv.FONT_HERSHEY_TRIPLEX.

Scale: 1.0.

Color: (0,255,0) → green.

Thickness: 2.
-----------------------------------------------------------------------------------------------------------------
#Always use cv.waitKey(0) to pause for images.

#Use cv.destroyAllWindows() to close all windows.

#cv.putText(img, text, position, font, scale, color, thickness)

#(0,255,0) → green, (0,0,255) → red, (255,0,0) → blue.

#cv.rectangle(img, pt1, pt2, color, thickness)

#cv.circle(img, center, radius, color, thickness)

#cv.line(img, pt1, pt2, color, thickness)

#np.zeros((h,w), dtype='uint8') → grayscale.

#np.zeros((h,w,3), dtype='uint8') → color (BGR).
