#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
=>Converts the image from BGR to grayscale.

Grayscale reduces complexity → useful for edge detection, thresholding, etc.
------------------------------------------------------------------------------------------------
#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
=>Smooths the image using a 7×7 Gaussian kernel.

Reduces noise and detail → better results for edge detection.
------------------------------------------------------------------------------------------------
#canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
=>Detects edges in the image.

Thresholds: 125 = min, 175 = max. 

1.Low threshold (125 here)

Any gradient value below 125 is considered not an edge → ignored.

2.High threshold (175 here)

Any gradient value above 175 is considered a strong edge → definitely an edge.

3.Values in between (125–175)

Considered weak edges.

Included only if they are connected to a strong edge
------------------------------------------------------------------------------------------------
#dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)
=>Dilation thickens edges → useful for emphasizing features.

iterations=1 → number of times dilation is applied.
------------------------------------------------------------------------------------------------

#eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)
=>Erosion thins edges → removes noise or unwanted dilation.

Tip: Common pattern: dilate → erode = morphological closing, erode → dilate = opening.

Dilate → Erode -Morphological Closing-	Fills small holes or gaps inside objects. Useful to close small black spots.
Erode → Dilate -Morphological Opening-	Removes small noise or unwanted white spots. Useful to clean up small white dots
-----------------------------------------------------------------------------------------------------
#resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)
=>Changes image dimensions to 500×500.

Can also use interpolation for quality: 
INTER_CUBIC: slowest, best quality.

INTER_LINEAR: default, fast.

INTER_AREA: best for shrinking images.
----------------------------------------------------------------------------------------------------

#cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
=>Crops a region of interest (ROI).

Format: img[y1:y2, x1:x2] → note that first is row (height), second is column (width).
----------------------------------------------------------------------------------------------------

#1. BGR vs Grayscale

BGR (Blue-Green-Red):

OpenCV loads color images in BGR format, not the more common RGB.

Shape of image array: (height, width, 3) → 3 channels for Blue, Green, Red.

Each pixel value ranges from 0–255 per channel.

Example: (0,255,0) → green in BGR.

Grayscale:

Single channel image, shape: (height, width).

Pixel values range 0–255 (0 = black, 255 = white).

Converting an image to grayscale reduces computational complexity, since algorithms only process one intensity channel instead of three color channels, while preserving the essential information needed for tasks like edge detection, thresholding, and morphological operations.

-----------------------------------------------------------------------------------------------------
#2. Noise Reduction before Edge Detection

Why: Edge detectors like Canny detect sharp intensity changes. Noise can create false edges.

Solution: Apply Gaussian Blur:

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
edges = cv.Canny(blur, 125, 175)


Gaussian Blur:

Smooths the image using a weighted average of neighboring pixels.

Kernel size controls the blur strength: (3,3) → mild, (7,7) → stronger.

Interview Tip:

Always mention “we blur first to reduce noise, then detect edges”.

Using a bigger kernel reduces small false edges but may slightly soften real edges.
--------------------------------------------------------------------------------------------
#3. Morphological Operations

Operate on binary or edge-detected images.

1.Dilation:

Thickens white regions (foreground).

Connects broken parts.
2.Erosion:

Thins white regions.

Removes small white noise.

Pattern	          Name	     Purpose
Dilate → Erode	 Closing	     Fill small holes in objects
Erode → Dilate	 Opening	     Remove small noise
--------------------------------------------------------------------------------------------
#4. Resizing and Interpolation

Resize to standard dimensions for processing or visualization

Interpolation Methods:
1.INTER_NEAREST: Fast, low quality.

2.INTER_LINEAR: Default, good quality for zoom in/out.

3.INTER_CUBIC: Slow, high quality (smooth edges, best for enlarging).

4.INTER_AREA: Best for shrinking images.
-----------------------------------------------------------------------------------------------
#5. Cropping

Extract Region of Interest (ROI)

Use Cases: Focus on a specific object in the image, reduce processing load.

Note: Rows → y, Columns → x.
-------------------------------------------------------------------------------------------------
#6. Pipeline Order Matters

Correct order:

Load image → 2. Blur → 3. Edge detection → 4. Morphological operations → 5. Resize/Crop/Display

Reason:

Blurring first reduces noise → prevents false edges.

Edge detection after blurring gives clean results.

Dilation/Erosion improves edges or removes small noise after detection.

Resizing/cropping is usually done at the end for visualization or further processing.
