import cv2
import numpy as np

ratio = 3/4
width = 640
vdo= cv2.VideoCapture(0,cv2.CAP_DSHOW)
vdo.set(3,width)
vdo.set(4,ratio*width)
vdo.set(10,150)

def empty(a):
	pass

cv2.namedWindow("HSV Trackbar")
cv2.resizeWindow("HSV Trackbar", 640, 240)
cv2.createTrackbar("HUE m","HSV Trackbar",0,179,empty)
cv2.createTrackbar("SAT m","HSV Trackbar",0,255,empty)
cv2.createTrackbar("VAL m","HSV Trackbar",0,255,empty)
cv2.createTrackbar("HUE M","HSV Trackbar",179,179,empty)
cv2.createTrackbar("SAT M","HSV Trackbar",255,255,empty)
cv2.createTrackbar("VAL M","HSV Trackbar",255,255,empty)

while True:
	success, img = vdo.read()
	imgBlur = cv2.GaussianBlur(img,(7,7),0)

	hm=cv2.getTrackbarPos("HUE m","HSV Trackbar")
	hM=cv2.getTrackbarPos("HUE M","HSV Trackbar")
	sm=cv2.getTrackbarPos("SAT m","HSV Trackbar")
	sM=cv2.getTrackbarPos("SAT M","HSV Trackbar")
	vm=cv2.getTrackbarPos("VAL m","HSV Trackbar")
	vM=cv2.getTrackbarPos("VAL M","HSV Trackbar")
	print(hm,sm,vm,hM,sM,vM)

	imgHSV = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2HSV)
	lower = np.array([hm,sm,vm])
	upper = np.array([hM,sM,vM])
	mask = cv2.inRange(imgHSV,lower,upper)

	#cv2.imshow("Orig", img)
	cv2.imshow("Mask", mask)


	if cv2.waitKey(1) & 0xFF == ord('e'):
		cv2.destroyAllWindows()
		break