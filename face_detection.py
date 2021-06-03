import cv2
import numpy as np
from PIL import Image 
cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, photo = cap.read()
    faces = model.detectMultiScale(photo)
    if len(faces)==0:
        pass
    else:
        x1 = faces[0][0]
        #print(x1)
        y1 = faces[0][1]
        x2 = x1 + faces[0][2]
        y2 = y1 + faces[0][3]
        aphoto = cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0],5)
        cv2.imshow('hii', aphoto)
        if cv2.waitKey(10)==13:
            break
cv2.destroyAllWindows()   
cap.release()     

img = Image.fromarray(aphoto ,"RGB")
img.save('tet.png')
img.show()
im = Image.open(r"tet.png")
im1 = im.crop((x1, y1, x2, y2))
im1.show()
im1.save('crop.png')