import cv
  
# ---------------------------
# Setup the webcam and font
# ---------------------------
  
# define image size
imageWidth = 320
imageHeight = 240
  
# create a window object
cv.NamedWindow("window1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
  
# create a camera object
capture = cv.CaptureFromCAM(camera_index)
  
# set capture width and height
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_WIDTH, imageWidth );
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_HEIGHT, imageHeight );
  
while True:
  
    # get image from webcam
    frame = cv.QueryFrame(capture)
  
    # -----------------------------
    # show the image on the screen
    # -----------------------------
    cv.ShowImage("window1", frame)
  
    # -----------------------
    # wait for user command
    # -----------------------
    command = cv.WaitKey(10)
  
    # if press 'q' -> exit program
    if command == ord('q'):
        print "Ending program"
        break  # end program
