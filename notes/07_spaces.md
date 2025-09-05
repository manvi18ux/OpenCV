#1. BGR (Blue, Green, Red)

Default format when you read an image using cv.imread().

OpenCV uses BGR instead of RGB.

Suitable for general image display and processing.

Limitation: Not intuitive for tasks like object detection by color.
--------------------------------------------------------------------------------------------------------
#2. RGB (Red, Green, Blue)

Standard color format for most libraries (like Matplotlib, PIL).

Used when displaying images with Matplotlib.

Conversion:

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)


Interview Point: Always convert BGR → RGB before plotting in Matplotlib, otherwise colors appear wrong (blue ↔ red swapped).
----------------------------------------------------------------------------------------------------------------
#3. Grayscale

Single channel (intensity only).

Size: (Height × Width) vs. (Height × Width × 3) for color images.

Advantages:

Reduces computational cost (1 channel vs 3).

Essential for edge detection, thresholding, feature extraction.

Conversion:

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
-----------------------------------------------------------------------------------------------------------------
#4. HSV (Hue, Saturation, Value)

Hue: type of color (0–179 in OpenCV).

Saturation: intensity of the color.

Value: brightness.

Use case: Object detection & color segmentation (e.g., detecting red objects under different lighting conditions).

Conversion:

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
--------------------------------------------------------------------------------------------------------------
#5. LAB (L*a*b*)

L*: Lightness

a*: Green → Red

b*: Blue → Yellow

Mimics human vision perception (perceptually uniform color space).

Use case: Color-based image enhancements, illumination invariance (better under varying lighting).

Conversion:

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
----------------------------------------------------------------------------------------------------------------
* OpenCV reads images in BGR by default.

* Grayscale reduces computational load → best for preprocessing in edge detection, thresholding, etc.

* HSV is robust for color detection (separates chromatic content from intensity).

* LAB is good for advanced tasks like image enhancement and color corrections.

Always remember:

* cv.imshow() works with BGR.

* plt.imshow() needs RGB → convert first.