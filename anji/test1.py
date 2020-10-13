import cv2
import numpy as np

path = 'img3.jpg'
img = cv2.imread(path)
img1 = cv2.imread(path,0)

def nothing(x):
  pass

def next1(img,edges,mask):
	x,y,w,h,x1,y1,w1,h1 = 0,0,0,0,0,0,0,0
	newx , newy = 0,0
	newx1 , newy1 = 0,0
	while True:
		contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		for c in contours:
			x,y,w,h = cv2.boundingRect(c)
			if w>70 and h>70: 
				cv2.rectangle(img,(x,y),(x+w,y+h),(155,155,0),5)
				newx = x
				newy = y
			# cv2.drawContours(img,contours,-1,(0,0,255),3) 
		cv2.line(img, (0,0), (x1,y1),(255,255,255) , 5)
		cv2.imshow("img",img)
		k = cv2.waitKey(1) & 0xFF

		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break

	while True:
		contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		for c in contours:
			x1,y1,w1,h1 = cv2.boundingRect(c)
			if w1>5 and h1>10: 
				cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(155,155,255),5)
				cv2.line(img, (0,0), (newx,newy),(255,255,255) , 5)
				cv2.line(img, (0,0), (x1,y1),(255,255,0) , 5)
				newx1 = x1
				newy1 = y1
                                #cv2.line(img, (len(img),len(img[0])), (x1,y1),(255,255,0) , 5)
                                
		cv2.imshow("img",img)
		k = cv2.waitKey(1) & 0xFF

		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break

	a = np.sqrt((0-newx)*(0-newx) + (0-newy)*(0-newy))
	b = np.sqrt((0-newx1)*(0-newx1) + (0-newy1)*(0-newy1))
	print('a',a,'\nb',b)


cv2.namedWindow('Colorbars')
hh='Max'
hl='Min'
wnd = 'Colorbars'

cv2.namedWindow('cvtbar')
hh='Max'
hl='Min'
wnd = 'cvtbar'


cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min", "Colorbars",0,255,nothing)
cv2.createTrackbar("ed1", "Colorbars",0,255,nothing)
cv2.createTrackbar("ed2", "Colorbars",0,255,nothing)

cv2.createTrackbar("r1", "cvtbar",0,255,nothing)
cv2.createTrackbar("g1", "cvtbar",0,255,nothing)
cv2.createTrackbar("b1", "cvtbar",0,255,nothing)
cv2.createTrackbar("r2", "cvtbar",0,255,nothing)
cv2.createTrackbar("g2", "cvtbar",0,255,nothing)
cv2.createTrackbar("b2", "cvtbar",0,255,nothing)



img = cv2.resize(img, (400,400), fx=0.5, fy=0.5)
img1 = cv2.resize(img1, (400,400), fx=0.5, fy=0.5)

thresh1 = np.array(img)
thresh2 = np.array(img)
edges = np.array(img)

while True:
	# ret, img = cap.read()
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hul=cv2.getTrackbarPos("Max", "Colorbars")
	huh=cv2.getTrackbarPos("Min", "Colorbars")

	ret,thresh1 = cv2.threshold(img1,hul,huh,cv2.THRESH_BINARY)
	ret,thresh2 = cv2.threshold(img1,hul,huh,cv2.THRESH_BINARY_INV)
	
	ed1=cv2.getTrackbarPos("ed1", "Colorbars")
	ed2=cv2.getTrackbarPos("ed2", "Colorbars")
	edges = cv2.Canny(thresh2,ed1,ed2)

	#CONVERT TO HSV COLORS
	
	r1=cv2.getTrackbarPos("r1", "cvtbar")
	g1=cv2.getTrackbarPos("g1", "cvtbar")
	b1=cv2.getTrackbarPos("b1", "cvtbar")

	r2=cv2.getTrackbarPos("r2", "cvtbar")
	g2=cv2.getTrackbarPos("g2", "cvtbar")
	b2=cv2.getTrackbarPos("b2", "cvtbar")

	lower_blue = np.array([r1,g1,b1])
	upper_blue = np.array([r2,g2,b2])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(img, lower_blue, upper_blue)

	# cv2.imshow(wnd)
	# cv2.imshow("thresh1",thresh1)
	cv2.imshow("thresh2",thresh2)
	cv2.imshow("edges",edges)
	cv2.imshow("mask",mask)

	k = cv2.waitKey(1) & 0xFF

	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break

cv2.destroyAllWindows()
next1(img,edges,mask)
