# Python program for blending of
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
a= cv2.imread('a.png', 1)

# Read image2
b = cv2.imread('b.png', 1)
c = cv2.imread('c.png', 1)
y = cv2.imread('y.png', 1)

one=c*41
two=a*21
three=b*3

img= y+one-two-three

# Show the image
cv2.imshow('image', img)
cv2.imwrite('d.jpeg', img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
