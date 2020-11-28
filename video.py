import cv2
print("System up and running...")

vdo=cv2.VideoCapture("test.mp4")

while True:	#video is nothing but a sequence of images
	success, img = vdo.read()
	cv2.imshow("Video output ",img)
	if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
		break