#def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  # width, height
    return cv.warpAffine(img, transMat, dimensions)
 => The transformation matrix [[1, 0, x], [0, 1, y]] shifts pixels.

Positive x → right, Negative x → left.

Positive y → down, Negative y → up.

💡 Use case: Aligning images, shifting objects for data augmentation.
---------------------------------------------------------------------------------------------
#def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

=>cv.getRotationMatrix2D(rotPoint, angle, scale) creates a 2×3 rotation matrix.

Positive angle → counter-clockwise.

Negative angle → clockwise.

Scale = 1.0 keeps size same (scaling allowed).

💡 Use case: Image augmentation, correcting tilted images.
-----------------------------------------------------------------------------------------------
#flip = cv.flip(img, 0)

=>0 → vertical flip (up-down).

1 → horizontal flip (left-right).

-1 → both axes.
---------------------------------------------------------------------------------------------------
#Image Shape in OpenCV

OpenCV reads images in the format (height, width, channels).

Example: (500, 700, 3) → 500 rows (height), 700 columns (width), 3 channels (BGR).

Important to remember: first index = rows (y), second index = columns (x).
----------------------------------------------------------------------------------------------------
#warpAffine() → Linear Transformations

Used for translation and rotation.

Works with a 2×3 transformation matrix.

Keeps image structure intact while moving/rotating pixels.

Formula behind it:


[𝑥'   = M* [x
𝑦']         y
            1]

where 
𝑀 is the transformation matrix.
--------------------------------------------------------------------------------------------
#Flipping simulates mirror views of objects (e.g., left-hand vs right-hand).

Cropping helps in training on specific regions of interest (ROI).

Both are essential to make ML models robust to variations.
--------------------------------------------------------------------------------------------
#Rotate → Crop: might cut out parts of rotated object.

Crop → Rotate: rotates only the ROI, leaving background out.

Key point: Always design the pipeline order based on your task.
-------------------------------------------------------------------------------------------
#OpenCV stores images as (height, width, channels). Using warpAffine(), we can apply translation and rotation as linear transformations. When resizing, interpolation choice is critical — cubic gives higher quality but is slower. Flipping and cropping are widely used in deep learning for data augmentation. And importantly, transformation order matters because operations are not commutative, e.g., rotating before cropping gives a different result than cropping before rotating.