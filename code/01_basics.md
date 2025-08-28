#OpenCV:  open source computer vision library.
         It helps to see, understand & process images or videos just like humans do with their eyes.

#Caer: A simpler wrapper around OpenCV + NumPy for easy computer vision tracks.

#cv.imread: read an image from your computer into your python program.

#cv.imshow: to display an image in a window.

#cv.VideoCapture: is used to open a video source like a camera or video file.
                  EX: cap = cv.VideoCapture() ->If you pass number(0,1,2 etc.), it tries to open a camera device.
                                              ->If you pass a string("video.mp4"), it tries to open a video file.
                 cv.VideoCapture(1) -> means it tells OpenCV to open the second camera on your system.
                                (0)  -> default webcam
                                (1)  -> external/second camera
                                (2)  -> third camera
                            
#cv.waitKey(0): waits for a key press from the keyboard. 0 means delay.


