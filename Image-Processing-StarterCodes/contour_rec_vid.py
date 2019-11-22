import numpy as np
import cv2

number = 1

#cap = cv2.VideoCapture('walk_'+ str(number) + '.mp4')
cap = cv2.VideoCapture('vid_'+str(number)+'.mp4')

first_frame = None

while(True):
	ret, img = cap.read()
	if img is None:
		break
	gray_new = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if first_frame is None:
		first_frame = gray_new.copy()
		continue

	img_diff = cv2.absdiff(gray_new, first_frame)

	ret, thresh = cv2.threshold(img_diff, 20, 255, 0)
	thresh = cv2.dilate(thresh, None, iterations = 1)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if number > 6:
		cv2.putText(img, 'NOT WALKING', (25, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
	else:
		if contours:
			largest_contour = max(contours, key= lambda x: cv2.contourArea(x))
			if cv2.contourArea(largest_contour) > 1000:
				x,y,w,h = cv2.boundingRect(largest_contour)
				cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 0)
				# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
				cv2.putText(img, 'WALKING', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
				# Cropp the rectangle and show it
				clone = thresh.copy()
				roi = clone[y:y+h, x:x+w]
				cv2.imshow("ROI", roi)
	cv2.imshow("thresh", thresh)

	#cv2.imshow('thresh', thresh)
	cv2.imshow('image', img)
	first_frame = gray_new.copy()
	key = cv2.waitKey(0)
	# if key == ord(' '):
	# 	cv2.waitKey(0)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()