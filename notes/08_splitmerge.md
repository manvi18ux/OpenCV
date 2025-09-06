#b, g, r = cv.split(img)

=>Separates the B, G, R channels.
Example:

b.shape → (height, width)

g.shape → (height, width)

r.shape → (height, width)
------------------------------------------------------------------------------------------------------------
#blue  = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red   = cv.merge([blank, blank, r])

=>By merging each single channel with two blank channels, we highlight that channel in color:

blue → shows only blue intensities in original image.

green → only green intensities.

red → only red intensities.
----------------------------------------------------------------------------------------------------------
#print(img.shape)   # (height, width, 3)
print(b.shape)     # (height, width)
print(g.shape)     # (height, width)
print(r.shape)     # (height, width)

=>img.shape → (height, width, 3) → 3D array (3 channels).

But after splitting:

b.shape → (height, width)

g.shape → (height, width)

r.shape → (height, width)

So each split channel is a 2D array (grayscale image), because you’re looking at just the intensity values of that channel.
👉 Example:
If your image is 600 × 800 pixels with 3 channels:

img.shape → (600, 800, 3)

b.shape → (600, 800)

g.shape → (600, 800)

r.shape → (600, 800)
---------------------------------------------------------------------------------------------------------------------
#merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

=>Combines B, G, R back into a 3-channel image.

Should look identical to the original image (img).
--------------------------------------------------------------------------------------------------------------------------
1.Why Split & Merge?

Splitting: Analyze or modify specific color components.

Example: Detecting objects based only on red channel.

Merging: Reconstruct original or modified image after processing channels individually.

2.Channel Representation:

Each channel is just a grayscale image where pixel intensity represents the strength of that color.

3.Practical Uses:

Image thresholding per channel (detect red objects, remove background, etc).

Enhancement (boosting one channel, reducing noise in another).

Data Augmentation in deep learning.