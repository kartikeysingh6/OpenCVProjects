import cv2
import random

faceCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
vdo=cv2.VideoCapture(0, cv2.CAP_DSHOW)
vdo.set(4,480)
vdo.set(10,100)
color = (0,0,255)
font = cv2.FONT_HERSHEY_SIMPLEX
count = 0

while True:
	success, img = vdo.read()
	img2 = img.copy()
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(imgGray,1.1,4)

	for(x,y,w,h) in faces:
		area = w*h
		if area>10000:
			cv2.rectangle(img2,(x,y),(x+w,y+h),color,2)
			cv2.putText(img2,"Detected:"+str(int(faces.size/4)),(0,20),font,0.7,color,2)
			imgRegOfInt = img[y:y+h,x:x+w]

	cv2.imshow("Result",img2)

	if cv2.waitKey(1) & 0xFF ==ord('s'):
		try:
			cv2.imwrite("Output_"+str(count)+".jpg",imgRegOfInt)
			cv2.rectangle(img2,(0,200),(640,300),(0,255,0),cv2.FILLED)
			cv2.putText(img2,"Snapshot Saved!",(150,265),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
			cv2.imshow("Result",img2)
			cv2.waitKey(500)
			count+=1
		except:
			cv2.rectangle(img2,(0,200),(640,300),(0,0,255),cv2.FILLED)
			cv2.putText(img2,"No Plate Detected!",(150,265),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)
			cv2.imshow("Result",img2)
			cv2.waitKey(500)
			count+=1

	elif cv2.waitKey(1) & 0xFF ==ord('e'):
		cv2.destroyAllWindows()
		break
