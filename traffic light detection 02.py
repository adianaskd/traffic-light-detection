import cv2
from ColorDetection import ColorDetection
cd=ColorDetection()
faceCascade= cv2.CascadeClassifier("haarcascades/cascade7.xml")
vid=cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
count=1
while True:
    res,img = vid.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,2) #imgname,scalefactor,nearest point
    # crop_img=img
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,0,0),2)
        crop_img=img[y:y+h,x:x+w]
        count+=1
        print("Traffic Light Found")
        cv2.imwrite("croped img/"+str(w) + str(h) + '_traffic'+str(count)+'.jpg', crop_img)
        path="croped img/"+str(w) + str(h) + '_traffic'+str(count)+'.jpg'
        print("output ",cd.detectColor(path))

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break