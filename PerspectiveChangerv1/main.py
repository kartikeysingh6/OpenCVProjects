import cv2 
import numpy as np

#to keep track of amount of points
count=0

#cordinates of points stored in a list
cordi = [0,0,0,0,0,0,0,0]
#cordi = [x1,y1, x2,y2, x3,y3, x4,y4]

def click_event(event, x, y, flags, params): 
    global count
    #if left mouse button is clicked and making sure count is <8(4x and 4y )
    if event == cv2.EVENT_LBUTTONDOWN and count<8:
        cordi[count]=x
        cordi[count+1]=y
        count+=2
        #showing cordinates of the clicked point 
        cv2.putText(img, str(x) + ',' +str(y), (x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8, (255, 255, 255), 1) 
        cv2.imshow('Image', img) 
      
    #if right mouse button is clicked
    if event==cv2.EVENT_RBUTTONDOWN:
        width,height = 400,600
        #cordinates of desired rectangle
        pt1 = np.float32([[cordi[0],cordi[1]],[cordi[2],cordi[3]],[cordi[4],cordi[5]],[cordi[6],cordi[7]]])
        #what refrence is the above cordinate
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        warpMatrix = cv2.getPerspectiveTransform(pt1,pt2)
        imgWarp = cv2.warpPerspective(imgorig,warpMatrix,(width,height))
        #shows the list of cordinates
        print(cordi)
        #shows the output 
        cv2.imshow("Output",imgWarp)
        #saves the output 
        cv2.imwrite("Output.jpeg",imgWarp)

if __name__=="__main__":
    path="img0.jpeg"
    imgorig = cv2.imread(path, 1) 
    img = cv2.imread(path, 1) 

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event) 
    cv2.waitKey(0) 
