import numpy as np
import cv2

cap=cv2.VideoCapture(0)

ret,frame=cap.read()
cv2.imwrite('raspPhoto.jpg',frame)

cap.release()
