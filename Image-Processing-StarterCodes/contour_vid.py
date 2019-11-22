import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 100, 255, 0)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	cv2.imshow('image', img)
	# 27 - ASCII for escape key
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()

