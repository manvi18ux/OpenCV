#kernel size is basically the number rows and columns.
----------------------------------------------------------------------------------------------------------
#average = cv.blur(img, (3,3))
=> Takes a 3×3 kernel and replaces each pixel with the average of its neighbors.

Very simple, but it tends to blur edges too much (loses detail).
------------------------------------------------------------------------------------------------------------
#gauss = cv.GaussianBlur(img, (3,3), 0)
=>Uses a Gaussian kernel (weights pixels near the center more than distant ones).

Produces a more natural blur compared to simple averaging.

Common for noise reduction before edge detection.
--------------------------------------------------------------------------------------------------------------
#median = cv.medianBlur(img, 3)
=>Replaces each pixel with the median value of its neighbors.

Very effective against salt-and-pepper noise (random white/black dots).

Preserves edges better than averaging.
------------------------------------------------------------------------------------------------------------
#bilateral = cv.bilateralFilter(img, 5, 15, 15)
=>More advanced filter:

Blurs the image while preserving edges.

Considers both spatial closeness and pixel intensity difference.

Used in tasks like cartooning, facial smoothing (keeps sharp edges intact).
---------------------------------------------------------------------------------------------------------
1.Averaging: Fast but not edge-preserving.

2.Gaussian Blur: Smooths noise, used in preprocessing (e.g., Canny edges).

3.Median Blur: Best for salt-and-pepper noise, keeps edges sharper.

4.Bilateral Filter: Edge-preserving blur, more computationally expensive.

⚡ Pipeline tip:

Before edge detection → Gaussian Blur.

For noisy images → Median Blur.

For edge-preserving smoothing → Bilateral.