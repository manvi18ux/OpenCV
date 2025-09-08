📌 Edge Detection Methods in OpenCV
1. Laplacian Operator

Computes the second derivative of the image.

Detects areas of rapid intensity change.

Sensitive to noise → usually used after blurring.

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))


cv.CV_64F prevents negative values from clipping.

Then converted to uint8 for display.

👉 Use case: Simple edge detection, highlighting regions of abrupt intensity change.
-----------------------------------------------------------------------------------------------------------------
2. Sobel Operator

Computes the first derivative (gradient).

Finds edges in horizontal (x) and vertical (y) directions.

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # x-direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # y-direction


cv.bitwise_or(sobelx, sobely) combines both.

👉 Use case: Better control (can detect vertical or horizontal edges separately).
------------------------------------------------------------------------------------------------------------------
3. Canny Edge Detection

More advanced pipeline:

Gaussian blur → gradient (Sobel) → non-maximum suppression → double threshold → hysteresis.

canny = cv.Canny(gray, 150, 175)


Produces thin, connected, and clean edges.

👉 Use case: Preferred in practice (e.g., object detection, contour finding).
---------------------------------------------------------------------------------------------------------------------
Laplacian = second derivative, simple but noisy.

Sobel = first derivative, gives edge direction (horizontal/vertical).

Canny = combines noise reduction + gradient detection + edge linking → most robust.
----------------------------------------------------------------------------------------------------------------
Difference between Sobel and Laplacian operators?
✅ Sobel uses first derivative → direction-aware, Laplacian uses second derivative → isotropic.

Why is Canny better than Laplacian/Sobel?
✅ Because it reduces noise, thins edges, and uses hysteresis to link weak edges → more accurate.

Why convert Laplacian to uint8?
✅ Because gradient values can be negative, np.absolute + uint8 ensures proper visualization.

When would you choose Sobel over Canny?
✅ If you specifically want edge orientation (horizontal/vertical).