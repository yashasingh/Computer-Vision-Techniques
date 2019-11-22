import numpy as np
import cv2

# Get the image
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Procesing
img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Show output
cv2.imshow('img-window', img2)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

