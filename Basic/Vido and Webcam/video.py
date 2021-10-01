import cv2

cap = cv2.VideoCapture("test.mp4")

while True:	
	#What this command does is that it reads lot of images per second
	#because a video is nothing but a sequence of images
	success, img = cap.read()
	print(success)
	cv2.imshow("Video Output",img)
	
	if cv2.waitKey(10) & 0xFF ==ord('x'):	#e to exit
		cv2.destroyAllWindows()
		break
