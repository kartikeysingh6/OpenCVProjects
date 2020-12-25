import cv2
import numpy as np

ratio = 3/4
width = 640
vdo= cv2.VideoCapture(0,cv2.CAP_DSHOW)
vdo.set(3,width)
vdo.set(4,ratio*width)
vdo.set(10,150)

myColors = [[168, 181, 0, 179, 255, 255]
			,[44,112,35,89,255,255]
			]
myColorVal = [[0,0,255]
			 ,[0,255,0]	
			]

myPoints = []	#x,y,colorID

def findColor(img,myColors,myColorVal):
	count = 0
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	newPoints=[]

	for color in myColors:
		#lower = np.array([h_min,s_min,v_min])
		lower = np.array(color[0:3])
		#upper = np.array([h_max,s_max,v_max])
		upper = np.array(color[3:6])
		mask = 	cv2.inRange(imgHSV,lower,upper)
		x,y = getContours(mask)
		cv2.circle(imgResult,(x,y),5,myColorVal[count],cv2.FILLED)
		if(x and y):
			newPoints.append([x,y,count])
		count+=1
		#cv2.imshow(str(color[0]), mask)
	return newPoints

def getContours(img):
	#external retrival method(retrives the extreme/outer contors)
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	x,y,w,h=0,0,0,0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area>500:
			#cv2.drawContours(imgResult,cnt,-1,(0,255,0),5)
			peri = cv2.arcLength(cnt,True)
			#resolution is 0.02*length of arc play with it, True becoz our shape is closed
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			x,y,w,h = cv2.boundingRect(approx)

	#we want tip and center
	return x+w//2,y

def drawOnCanvas(myPoints,myColorVal):
	for point in myPoints:
		cv2.circle(imgResult,(point[0],point[1]),10,myColorVal[point[2]],cv2.FILLED)


while True:
	success, img = vdo.read()
	imgResult = img.copy()
	newPoints = findColor(img,myColors,myColorVal)

	if(len(newPoints)):
		for newP in newPoints:
			myPoints.append(newP)

	if len(myPoints):
		drawOnCanvas(myPoints,myColorVal)

	cv2.imshow("Result",imgResult)
	
	if cv2.waitKey(1) & 0xFF ==ord('e'):
		cv2.destroyAllWindows()
		break
