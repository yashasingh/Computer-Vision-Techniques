import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray_old = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while(True):
	ret, frame = cap.read()
	gray_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	img_diff = cv2.absdiff(gray_new, gray_old)
	cv2.imshow('Result', img_diff)
	cv2.imshow('Old', gray_old)
	cv2.imshow('New', gray_new)
	gray_old = gray_new.copy()
	if cv2.waitKey(1) == ord(' '):
		cv2.waitKey(0)
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()