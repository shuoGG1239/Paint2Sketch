import cv2
import numpy as np


def inverse_color(image):
    height,width = image.shape
    img2 = image.copy()
    for i in range(height):
        for j in range(width):
            img2[i,j] = (255-image[i,j]) 
    return img2

IMG_PATH = "test (4).jpg"

img = cv2.imread(IMG_PATH)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("Canny-Contour", inverse_color(img))
cv2.waitKey(0)
cv2.destroyAllWindows()
