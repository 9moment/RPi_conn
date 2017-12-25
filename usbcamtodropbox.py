import cv
import datetime
import RPi.GPIO as GPIO
import time
import commands
from subprocess import call
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
  
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
  
# create a font
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX_SMALL , 0.5, 0.5, 0, 1, cv.CV_AA)
 
while True:
  
    # get image from webcam
    frame = cv.QueryFrame(capture)
  
    # -------------------------------------------
    # Draw the time stamp on a white background
    # -------------------------------------------  
    cv.Rectangle(frame, (0,0), (imageWidth, 15), (255,255,255),cv.CV_FILLED,8,0)
    # get the current date and time
    timeStampString = datetime.datetime.now().strftime("%A_%Y-%m-%d-%H:%M:%S")
    # insert the date time in the image
    cv.PutText(frame, timeStampString, (10,10), font, (0,0,0))
  
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
    elif command == ord('s'):
        print "Saving image"
        cv.SaveImage(timeStampString + " p.jpg",frame)
    elif(GPIO.input(11) == 0):
        print "Saving image by button"
        cv.SaveImage(timeStampString + ".jpg",frame) 
        print ("File name \"" + timeStampString + ".jpg\"")
        print ("uploading please wait...")
        photofile = "Dropbox-Uploader/dropbox_uploader.sh upload %s.jpg /image" %  timeStampString          
        call ([photofile], shell=True)  
        print ("===================================================================")      
        time.sleep(1)
