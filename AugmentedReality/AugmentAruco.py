import cv2
import cv2.aruco as aruco
import numpy as np 
import os

imgaugDef = cv2.imread("show/def.jpg")
IDname = {
  83: "Lady Liberty",
  107: "Taj Mahal",
  196: "Eiffel Tower",
}

def findAruco(img, markersize=6,totalmarkers=250,draw=True):
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	key = getattr(aruco,f'DICT_{markersize}X{markersize}_{totalmarkers}')
	arucoDictionary = aruco.Dictionary_get(key)
	arucoParameters = aruco.DetectorParameters_create()
	bboxs,ids,rejected = aruco.detectMarkers(imgGray,arucoDictionary,parameters=arucoParameters)

	#print(ids)
	if draw:
		aruco.drawDetectedMarkers(img, bboxs)

	return [bboxs,ids]

def augmentAruco(bbox,id,nam,img,imgaug,drawID=True):
	
	topleft = 	  bbox[0][0][0], bbox[0][0][1]
	topright = 	  bbox[0][1][0], bbox[0][1][1]
	bottomright = bbox[0][2][0], bbox[0][2][1]
	bottomleft =  bbox[0][3][0], bbox[0][3][1]

	h,w,chnel = imgaug.shape

	#warp prespective
	pts1 = np.array([topleft,topright,bottomright,bottomleft])
	pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])

	matrix, _ = cv2.findHomography(pts2,pts1)
	imgout = cv2.warpPerspective(imgaug,matrix, (img.shape[1],img.shape[0]))
	cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
	imgout = img + imgout

	if drawID:
		cv2.putText(imgout, nam, topleft, cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)

	return imgout


def main():
	cap = cv2.VideoCapture(0)

	while(True):
		success,img=cap.read()
		arucofound = findAruco(img)

		#loop through all markers and augment them
		if len(arucofound[0])!=0:
			for bbox,id in zip(arucofound[0], arucofound[1]):
				#print(id)
				try:
					img = augmentAruco(bbox,id,IDname[id[0]],img,cv2.imread("show/"+str(id[0])+".jpg"))
				except:
					img = augmentAruco(bbox,id,str(id[0]),img,imgaugDef)

		cv2.imshow("Img",img)
		
		if cv2.waitKey(1) & 0xFF ==ord('e'):	#e to exit
			cv2.destroyAllWindows()
			break

if __name__ == "__main__":

	main()
