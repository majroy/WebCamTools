import numpy as np
import cv2
import time

cap1 = cv2.VideoCapture(0) #offset if there's a built in webcam
cap1.set(4,1080) #or 1024 or 1080
cap1.set(3,1920) #or 1280 or 1920

x = 10 #position of text
y = 150 #position of text
text_color = (255,0,0)
sfactor=1050.0 #must be declared as a real, width of output windows

def imposeXhair(cap,fps):
        
    # Capture frame-by-frame
    ret,frame=cap.read()
    
    
    # Perform operations on the frame
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        gray = np.zeros(np.shape(frame))


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

    
    cv2.putText(gray, "FPS: %3.2f"%fps, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=1)

    
    return gray

#main loop
fps=0 #initialize    
while(True):
    instant1=time.time()
    gray1=imposeXhair(cap1,fps)
    #fps calc tried in case of divide by zero
    try: 
        fps=1/(time.time()-instant1)
    except:
        pass

    cv2.imshow('Camera on 0',gray1)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('p'):
        cv2.imwrite('00.png',gray1)
        break
    if key & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cv2.destroyAllWindows()