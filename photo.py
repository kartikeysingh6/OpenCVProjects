import cv2
print("System up and running...")

img=cv2.imread("test.jpg")


cv2.imshow("Out fucking put",img)

#to stop image from vanishing in ms, 0for infinite dealy other values for delay in ms
cv2.waitKey(0)	

