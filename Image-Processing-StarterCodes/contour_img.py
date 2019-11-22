import numpy as np
import cv2

img = cv2.imread('yashapp.jpg')

# Making Binary Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
	cv2.drawContours(img, contours, i, (0, 255, 0), 3)
print(len(contours))

cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
