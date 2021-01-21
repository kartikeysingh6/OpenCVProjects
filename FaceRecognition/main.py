import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("Database/Elon.jpg")
imgElon = cv2.CvtColor(imgElon,cv2.COLOR_BGR2RBG)
imgTest = face_recognition.load_image_file("test.jpg")
imgTest = cv2.CvtColor(imgElon,cv2.COLOR_BGR2RBG)

faceLoc = face_recognition.face_location(imgElon)[0]
EncodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangel(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),2)

cv2.imshow("Elon Database",imgElon)
cv2.imshow("Elon Selfie", imgTest)
cv2.waitKey(0)