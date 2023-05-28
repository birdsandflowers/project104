import cv2

image=cv2.imread('solar-system.jpg')



cv2.putText(image,"Sun",(100,100),cv2.FONT_HERSHEY_COMPLEX,1.3,(255,0,0),2)
cv2.putText(image,"Mercury",(120,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Venus",(200,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Earth",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Mars",(370,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Jupiter",(550,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Saturn",(720,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.putText(image,"Neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)









cv2.imshow('output window',image)
cv2.waitKey(5000)
