import time
import cv2
import numpy as np
from datetime import datetime
import threading
import queue

def GetBoxParam():
    video = cv2.VideoCapture(0)

    _,frame = video.read()
    video.release()
    
    rows   = 4
    colums = 4
    
    boxes = []
    height = len(frame)//(rows)
    width = len(frame[0])//(colums)
#     print ('width',width)
#     print ('height',height)
    
    for i in range  ( 0 , len(frame)  , height ):
        for j in range ( 0 , len(frame[0])  , width ):
            param =[j,i,j+width,i+height]
#             print (param)
        
            boxes.append(param)
    return boxes

def segmentPart(X1,nn):
    
    x1 = int (X1[0])
    y1 = int (X1[1])
    x2 = int (X1[2])
    y2 = int (X1[3])

    while True:
        res,frame = video.read()    
        frame = frame[y1:y2,x1:x2]
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (9,9), 0)
        thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)[1]
    
        contours,_  = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours)==0:
            print (nn)
            now = datetime.now()
            print("now =", now)
            returns [nn] = now
            break
            # else:
                
        # count = 0
        # for i in range (len(thresh)):
        #     for j in range (len(thresh[0])):
        #         if thresh[i,j]>100:
        #             count +=1
        # if count > 100000:
        #     print ('nn',nn)

        cv2.imshow(str(nn),thresh)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

    return nn,now

video = cv2.VideoCapture(0)
if __name__ ==  '__main__':
    A = GetBoxParam()
    B = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    global returns
    returns = {}
    j=0
    no_of_td = []
    for i in A:
    	t = threading.Thread(target=segmentPart,name = 'thread '+str(B[j]),args=(i,B[j]))
    	t.start()
    	j+=1
    	no_of_td.append(t)

    for i in no_of_td:
    	a = i.join()

    print (returns)

    video.release()
    cv2.destroyAllWindows()
