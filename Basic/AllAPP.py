import cv2
import numpy as np
#Unlike maths y axis in open cv is down but x axis is same i.e towards right
#in open cv color scheme is nor RGB but BGR

#path = input("Enter Path: ")
path = "C:/Users/Kartikey/Desktop/Projects/OpenCV/PerspectiveChangerv1/img2.jpeg"
path2 = "C:/Users/ASUS/Downloads/iiitb.jpg"
kernel = np.ones((5,5),np.uint8)

img = cv2.imread(path)
img2 = cv2.imread(path2)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2Gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

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

#operations
imgand = cv2.bitwise_and(img2Gray, imgGray, mask = None)
imgor = cv2.bitwise_or(img2Gray, imgGray, mask = None)
imgxor = cv2.bitwise_xor(img2Gray, imgGray, mask = None)
imgxnor = cv2.bitwise_not(imgxor, mask = None)
imgnand = cv2.bitwise_not(imgand, mask = None)
not1 = cv2.bitwise_not(imgGray, mask = None)
not2 = cv2.bitwise_not(img2Gray, mask = None)
coloradd=imgand = cv2.add(img, img2, mask = None)
colorsub=imgand = cv2.subtract(img, img2, mask = None)
colormulti=imgand = cv2.multiply(img, img2)
colordiv=imgand = cv2.divide(img, img2)

print("Image Dimension(h, w, 3): " + str(img.shape))
print("Resized Image Dimension(h, w, 3): " + str(imgResize.shape))
print("Cropped Image Dimension(h, w, 3): " + str(imgCropped.shape))

cv2.imwrite("Gray.jpg",imgGray)
cv2.imwrite("Blur.jpg",imgBlur)
cv2.imwrite("Canny.jpg",imgCanny)
cv2.imwrite("Dilation.jpg",imgDilation)
cv2.imwrite("Erosion.jpg",imgErosion)
cv2.imwrite("Resize.jpg",imgResize)
cv2.imwrite("Cropped.jpg",imgCropped)
cv2.imwrite("CannyDilation.jpg",imgCannyDilation)
cv2.imwrite("CannyErosion.jpg",imgCannyErosion)
cv2.imwrite("CannyDialationThenErosion.jpg",imgCannyDialThenErosion)
