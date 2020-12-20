import cv2
import random

print("Press 'E' to exit!")

r=0
hit=0
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vdo=cv2.VideoCapture(0, cv2.CAP_DSHOW)	#CAP_DSHOW doesn't shows us warning of cap_msmf.cpp
vdo.set(3,640)	#width id is 3
vdo.set(4,480)	#height id is 4
vdo.set(10,100)	#brightness id is 10

while True:	#video is nothing but a sequence of images
	if r>256:
		hit=1
	if r<0:
		hit=0

	if hit==1:
		r-=5
	if hit==0:
		r+=5

	success, img = vdo.read()
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(imgGray,1.1,4)

	for(x,y,w,h) in faces:

		print(str(int(faces.size/4)) + " faces detected")

		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,r),2)
	
	cv2.imshow("Result",img)
	
	if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
		cv2.destroyAllWindows()
		break