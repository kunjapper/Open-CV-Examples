import random
import cv2

img = cv2.imread('assets/logo.jpg', -1)

print(img[257][45:400])

#print(img.shape)
# arrays and manipulating them
# Shape has a value like (995, 1000, 3)
#995 rows, 1000 columns, 3 channels
#channel is color space of the pixel
# Open cv is blue green red 0-255
# 
'''
for i in range (100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
'''

tag = img[500:700, 600:900]
img[100:300,650:950] = tag


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
