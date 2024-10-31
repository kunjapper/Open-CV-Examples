import cv2

img = cv2.imread('assets/logo.jpg', 0)
img = cv2.resize(img, (0,0), fx=1, fy=1)
cv2.imwrite('new_img.jpg', img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



