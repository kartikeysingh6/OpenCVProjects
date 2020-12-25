import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
file = open("output.txt","a")
img = cv2.imread("test.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
himg,wimg,k = img.shape

file.write(pytesseract.image_to_string(img))

#Detecting Characters
box = pytesseract.image_to_boxes(img)
for b in box.splitlines():
	b=b.split(' ')
	ch,x1,y1,x2,y2 = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
	cv2.putText(img,ch,(x1,himg-y1-41),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
	cv2.rectangle(img,(x1,himg-y1),(x2,himg-y2),(255,0,255),2)

#Detecting Words
box = pytesseract.image_to_data(img)
print(box)

cv2.waitKey(0)
