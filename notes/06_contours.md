#contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
=> Contours: boundaries of objects (lists of points).

Parameters:

cv.RETR_LIST: retrieves all contours (no hierarchy).

cv.CHAIN_APPROX_NONE: stores all points of contour.
(Alternative: CHAIN_APPROX_SIMPLE → compresses horizontal/vertical points).

len(contours) gives total number of detected contours.
------------------------------------------------------------------------------------------------
#cv.drawContours(blank, contours, -1, (0,0,255), 2)
=>Draws all contours (-1) on the blank image.

Color = (0,0,255) (red).

Thickness = 2.