import numpy as np
import cv2
import time

cap1 = cv2.VideoCapture(0) #offset if there's a built in webcam
cap2 = cv2.VideoCapture(1)
cap1.set(4,1024) #or 1080
cap1.set(3,1280) #or 1920

cap2.set(4,1024) #or 1080
cap2.set(3,1280) #or 1920

x = 10 #position of text
y = 20 #position of text
text_color = (255,0,0)
sfactor=850.0 #must be declared as a real, width of output windows

def imposeXhair(cap,fps):
        
    # Capture frame-by-frame
    ret,frame=cap.read()
    
    # Perform operations on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # #to rotate
    # height, width = gray.shape
    # M=cv2.getRotationMatrix2D((width/2,height/2),90,1)
    # gray = cv2.warpAffine(gray,M,(width,height))

    #resize the image
    r=sfactor/gray.shape[1]
    dim=(int(sfactor),int(gray.shape[0]*r))
    gray=cv2.resize(gray,dim,interpolation=cv2.INTER_AREA)
    height, width = gray.shape

    #create two crosshairs
    cv2.line(gray,(0,0),(width,height),(255,255,255),1)
    cv2.line(gray,(0,height),(width,0),(255,255,255),1)
    
    #create an array of marker pips centered on the image 
    for j in np.linspace(-20,20,5):
        cv2.line(gray,(int(width/2+j),int(height/2-5)),(int(width/2+j),int(height/2+5)),(255,255,255),1)
        
    #or a rectangle of a known size centred in the middle of the field
    # cv2.rectangle(gray,(width/2-10,height/2-10),
    # (width/2+10,height/2+10),(255,255,255),1)
    
    cv2.putText(gray, "FPS: %3.2f"%fps, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)

    
    return gray

#main loop
fps1=fps2=0 #initialize    
while(True):
    instant1=time.time()
    gray1=imposeXhair(cap1,fps1)
    end1=time.time()
    fps1=1/(end1-instant1)
    
    instant2=time.time()
    gray2=imposeXhair(cap2,fps2)
    end2=time.time()
    fps2=1/(end2-instant2)

    
    cv2.imshow('Camera on 0',gray1)
    cv2.imshow('Camera on 1',gray2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
cv2.destroyAllWindows()