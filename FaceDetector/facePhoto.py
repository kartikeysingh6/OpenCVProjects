import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("lenax.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:

	print(str(int(faces.size/4)) + " faces detected")

	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)
