import cv2
import numpy as np
def mouse(event, x, y, flags, params):
    print(x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        Fallaste=True
        circles.append((x, y))            
        if (x>=100 and x<=150 and y>=100 and y<=150):
            print("Rojo Muerto",x,y)
            Fallaste=False
        if (x>=151 and x<=201 and y>=100 and y<=150):
            print("Verde Muerto",x,y)
            Fallaste=False
        if (x>=202 and x<=252 and y>=100 and y<=150):
            print("Azul Muerto",x,y)
            Fallaste=False
        if (x>=253 and x<=303 and y>=100 and y<=150):
            print("Negro Muerto",x,y)
            Fallaste=False
        if Fallaste==True:
            print("Fallastes",x,y)
        cv2.circle(frame, (x,y), 5, (255, 0, 255), 0)
    
cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)
circles = []

while True:
    _, frame = cap.read()
    for center_position in circles:
        cv2.circle(frame, center_position, 3, (0, 255, 255), -1)
    cv2.rectangle(frame,(100,100),(150,150),(0,0,255),1)
    cv2.rectangle(frame,(151,100),(201,150),(0,255,0),1)
    cv2.rectangle(frame,(202,100),(252,150),(255,0,0),1)
    cv2.rectangle(frame,(253,100),(303,150),(0,0,0),1)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circles = []
cap.release()
cv2.destroyAllWindows()
