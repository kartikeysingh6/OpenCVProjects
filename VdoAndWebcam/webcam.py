import cv2
print("System up and running...")

vdo=cv2.VideoCapture(0, cv2.CAP_DSHOW)	#doesn't shows warning
vdo.set(3,640)	#width id is 3
vdo.set(4,480)	#height id is 4
vdo.set(10,100)	#brightness id is 10

while True:	#video is nothing but a sequence of images
	success, img = vdo.read()
	cv2.imshow("Video output ",img)
	
	if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
		cv2.destroyAllWindows()
		break
