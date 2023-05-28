import cv2

image=cv2.imread('poster.jpg')

rocket=image[120:360,400:500]
image[0:240,500:600]=rocket


cv2.putText(image,"Michelle",(100,100),cv2.FONT_HERSHEY_COMPLEX,1.3,(255,0,0),2)


cv2.imshow('output window',image)
cv2.waitKey(5000)