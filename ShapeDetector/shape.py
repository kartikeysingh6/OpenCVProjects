import cv2
import numpy as np
from stack import *

def getContours(img):
	#external retrival method(retrives the extreme/outer contors)
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for x in contours:
		area = cv2.contourArea(x)
		#print("A: " +str(area))

		#for reducing noise
		if area>1000:
			#cv2.drawContours(img2,x,-1,(0,255,0),5)
			peri = cv2.arcLength(x,True)
			#print("P: " +str(peri))
			#resolution is 0.02*length of arc play with it, True becoz our shape is closed
			approx = cv2.approxPolyDP(x,0.02*peri,True)
			objCorner = len(approx)
			x,y,w,h = cv2.boundingRect(approx)

			if objCorner==3:
				objType="Triangle"
			elif objCorner==4:
				#deviation of 15%
				ratio = w/float(h)
				if ratio > 0.85 and ratio < 1.15:
					objType="Square"
				else:
					objType="Rectangle"
			else:
				objType="Circle"

			#cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,0),2)
			cv2.putText(img2,objType,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)


path="shapes.png"

img = cv2.imread(path)
img2 = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur, 30,30)
imgBlank = np.ones_like(img)
getContours(imgCanny)

cv2.imshow("Joe ass!",img2)
cv2.waitKey(0)
