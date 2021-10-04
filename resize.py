import cv2

img = cv2.imread(r"C:\Users\user\Downloads\dog.jpg", 1)

resize = cv2.resize(img, (32,32))
cv2.imwrite(r'C:\Users\user\Downloads\dog2.jpg',resize)