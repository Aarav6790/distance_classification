import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Dr_Shashi_Tharoor.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')
plt.show()