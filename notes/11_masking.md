1.Masking is selecting a region of interest (ROI) from an image.

2.The mask is always a single-channel (grayscale) binary image:

White (255) → keep this region.

Black (0) → ignore this region.

3.Applications of Masking:

> Focus on specific areas (e.g., detect face only in an image).

> Shape-based cropping (circles, polygons).

> Preprocessing before feature extraction (like edge detection in ROI).

> Removing background.

✅ Quick takeaway:

Masking = AND operation with binary mask.

Powerful for object isolation and ROI selection.