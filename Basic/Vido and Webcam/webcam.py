import cv2

vdo=cv2.VideoCapture(0, cv2.CAP_DSHOW)
vdo.set(3,640)	#width id is 3
vdo.set(4,480)	#height(more chars) id is 4
vdo.set(10,100)	#brightness(10chars) id is 10

while True:	#video is nothing but a sequence of images
	success, img = vdo.read()
	cv2.imshow("Result",img)
	
	if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
		cv2.destroyAllWindows()
		break