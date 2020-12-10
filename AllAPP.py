import cv2
import numpy as np
#Unlike maths y axis in open cv is down but x axis is same i.e towards right
#in open cv color scheme is nor RGB but BGR

path = input("Enter Path: ")
#path = "H:/Photos/myoldpc.jpg"
name = "mypc"
kernel = np.ones((5,5),np.uint8)

img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Kerenal size of (7,7) has to be odd 3,3; 5,5 etc.. then sigma value generally 0
imgBlur = cv2.GaussianBlur(img,(7,7),0)
#We've to add 2 threshold values.
imgCanny = cv2.Canny(img,150,200)
imgDilation = cv2.dilate(img,kernel,iterations=1)
imgErosion = cv2.erode(img,kernel,iterations=1)
imgResize = cv2.resize(img,(100,300))	#w,h
imgCropped = img[20:240,160:385]		#h[:],w[:]

imgCannyErosion = cv2.erode(imgCanny,kernel,iterations=1)
imgCannyDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgCannyDialThenErosion = cv2.erode(imgCannyDilation,kernel,iterations=1)

print("Image Dimension(h, w, 3): " + str(img.shape))
print("Resized Image Dimension(h, w, 3): " + str(imgResize.shape))
print("Cropped Image Dimension(h, w, 3): " + str(imgCropped.shape))

cv2.imwrite(name + "Gray.jpg",imgGray)
cv2.imwrite(name + "Blur.jpg",imgBlur)
cv2.imwrite(name + "Canny.jpg",imgCanny)
cv2.imwrite(name + "Dilation.jpg",imgDilation)
cv2.imwrite(name + "Erosion.jpg",imgErosion)
cv2.imwrite(name + "Resize.jpg",imgResize)
cv2.imwrite(name + "Cropped.jpg",imgCropped)
cv2.imwrite(name + "CannyDilation.jpg",imgCannyDilation)
cv2.imwrite(name + "CannyErosion.jpg",imgCannyErosion)
cv2.imwrite(name + "CannyDialationThenErosion.jpg",imgCannyDialThenErosion)