1. What is the difference between simple and adaptive thresholding?

✅ Answer:

Simple Thresholding uses a global fixed threshold for the entire image. It works only if illumination is uniform.

Adaptive Thresholding calculates the threshold locally for each small region based on the neighborhood mean or weighted mean (Gaussian). It is better for images with varying lighting conditions.
------------------------------------------------------------------------------------------------------------------------------
2. Why do we usually convert images to grayscale before thresholding?

✅ Answer:

Thresholding operates on intensity values.

Grayscale has only one channel (0–255), while color images have 3 channels (BGR).

Working in grayscale reduces computational complexity and avoids ambiguity in thresholding across channels.
---------------------------------------------------------------------------------------------------------------------------------
3. What does the parameter C do in adaptiveThreshold()?

✅ Answer:

C is a constant subtracted from the mean (or Gaussian-weighted sum).

It helps fine-tune the threshold:

A larger C → makes threshold slightly lower → more pixels become white.

A smaller C (or 0) → threshold closer to mean → stricter segmentation.
-------------------------------------------------------------------------------------------------------------------------------
4. In which real-world cases would you use adaptive thresholding over simple thresholding?

✅ Answer:

OCR (Optical Character Recognition) for scanned documents with uneven lighting.

Medical imaging where illumination varies across regions.

Object detection in outdoor scenes with shadows and brightness variations.
-----------------------------------------------------------------------------------------------------------------------------
Thresholding is often a preprocessing step → before edge detection, contour extraction, or text recognition.

Always pair with blurring/denoising to improve results.