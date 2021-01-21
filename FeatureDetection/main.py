import cv2
import numpy as np 
import os

path = "ImagesQuery"
#orb(feature detection algo) is fast and most importantly FREE
#swift and surf are expensive
#orb finds about 500 features(default) in figure cross check it by ds1.shape
orb = cv2.ORB_create(nfeatures=1000)

images = []
classnames = []
mylist = os.listdir(path)
print("Total Classes:", len(mylist))

for cl in mylist:
	#0 imports it as gray scale
	imgCur = cv2.imread(f'{path}/{cl}',0)
	images.append(imgCur)
	#classnames.append(os.path.splitext(cl)[0]
	classnames.append(cl.split('.')[0])

print(classnames)

def findDes(images):
	desList = []
	for img in images:
		#none for mask, ds is descriptor
		kp,des = orb.detectAndCompute(img,None)
		desList.append(des)
	return desList

def findID(img,desList):
	kp2,des2 = orb.detectAndCompute(img,None)
	BF = cv2.BFMatcher()
	matchList=[]

	try:
		for des in desList:
			matches = BF.knnMatch(des,des2,k=2)	#k=2, coz we want 2 values that we can compare later on
			good =[]
			for m,n in matches:
				if m.distance < 0.75*n.distance:
					good.append([m])
			matchList.append(len(good))
		
		max_ele=matchList[0]
		max_ind=0
		for i in range(1,len(matchList)):
			if max_ele<matchList[i]:
				max_ele=matchList[i]
				max_ind=i
		if max_ele > 15:
			global txt
			txt = classnames[max_ind]
		else:
			txt = ""
	except:
		txt = ""

desList = findDes(images)
print(len(desList))

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
	success, img2=cap.read()
	imgorig = img2.copy()
	img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	findID(img2,desList)
	cv2.putText(imgorig,txt,(70,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

	cv2.imshow("Inp",imgorig)
	
	if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
		cv2.destroyAllWindows()
		break
	

#Out img as none
# imgkp1 = cv2.drawKeypoints(img1,keypnt1,None)
# imgkp2 = cv2.drawKeypoints(img2,keypnt2,None)

#now we can compare the 2 descriptors to see how much of similarity is there b/w 2 imgs
#we can use traditional BruteForce method but it's not optimal insted we'll use k neighbours BF




# img3 = cv2.drawMatchesKnn(img1,keypnt1,img2,keypnt2,good,None,flags=2)	#out img none

# cv2.imshow("kp1",imgkp1)
# cv2.imshow("kp2",imgkp2)
# cv2.imshow("img3",img3)
# cv2.waitKey(0)
