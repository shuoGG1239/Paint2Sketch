import cv2
import numpy as np

IMG_PATH = "test (4).jpg"

img = cv2.imread(IMG_PATH)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("Canny-Contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
