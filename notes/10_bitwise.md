#rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle    = cv.circle(blank.copy(), (200,200), 200, 255, -1)
=>rectangle → white filled square (value 255 = white, on black background).

circle → white filled circle.

Both stored as binary masks (0 = black, 255 = white).
----------------------------------------------------------------------------------------------------------------------
AND → intersection

OR → union

XOR → difference (excluding overlap)

NOT → invert