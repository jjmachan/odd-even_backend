import cv2
import os

img = cv2.imread("./images/train/FIVE/FIVE_0.png")
print(img.shape)
cv2.imshow("image",img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.GaussianBlur(img, (7,7), 3)
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#ret, new = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("image processed",img)
cv2.waitKey(0)
