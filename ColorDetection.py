import cv2
import numpy as np
class ColorDetection:
  def __init__(self):
    a=7
  def detectColor(self,path):
    img = cv2.imread(path)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernal = np.ones((5,5), "uint8")

    # print("HSV image matrix:\n")
    # print(imgHSV)
    # red color
    red_lower = np.array([0, 115, 14], np.uint8)
    red_upper = np.array([2, 255, 255], np.uint8)
    red_mask = cv2.inRange(imgHSV, red_lower, red_upper)
    red_mask =cv2.dilate(red_mask,kernal)
    red_result=cv2.bitwise_and(img,img,mask=red_mask)
    # cv2.imshow("RED",red_result)

    #amber color
    amber_lower = np.array([21, 129, 43],np.uint8)
    amber_upper = np.array([26, 255, 255],np.uint8)
    amber_mask=cv2.inRange(imgHSV,amber_lower,amber_upper)
    amber_mask =cv2.dilate(amber_mask,kernal)
    amber_result=cv2.bitwise_and(img,img,mask=amber_mask)
    # cv2.imshow("AMBER",amber_result)

    # green color
    green_lower = np.array([47,147, 10],np.uint8)
    green_upper = np.array([102, 255, 255],np.uint8)
    green_mask=cv2.inRange(imgHSV,green_lower,green_upper)
    green_mask =cv2.dilate(green_mask,kernal)
    green_result=cv2.bitwise_and(img,img,mask=green_mask)
    # cv2.imshow("GREEN",green_result)
    f=1
    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
    if f==1:
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 1000):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), 
                                            (x + w, y + h), 
                                            (0, 0, 255), 2)
                return ("STOP")
                f=0
                cv2.putText(img, "STOP", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (0, 0, 255))
                break


    contours, hierarchy = cv2.findContours(amber_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
    if f==1:
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 1000):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), 
                                            (x + w, y + h), 
                                            (0, 0, 255), 2)
                return("GET READY")
                f=0
                cv2.putText(img, "GET READY", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (0, 0, 255))
    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
    if f==1:
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 10):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), 
                                            (x + w, y + h), 
                                            (0, 0, 255), 2)
                return("GO")
                f=0
                cv2.putText(img, "Go", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                            (0, 0, 255))
