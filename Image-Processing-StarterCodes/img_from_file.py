import numpy as np
import cv2

# Get the image
img1 = cv2.imread('yashapp.jpg')

# Do the processing
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Show the output
cv2.imshow('yashapp', img2)

# Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
