import cv2

cap = cv2.VideoCapture("test.mp4")

while True:	#video is nothing but a sequence of images
	success, img = cap.read()
	cv2.imshow("Video",img)
	
	if cv2.waitKey(10) & 0xFF ==ord('e'):	#e to exit
		cv2.destroyAllWindows()
		break