import cv2
img = cv2.imread("image/shutterstock_669619393.jpg")
imgresize = cv2.resize(img, (800, 500))

# ภาพ จุดเริ่มต้น จุดสิ้นสุด สี เส้นหนา
cv2.line(imgresize, (100, 100), (800, 500), (255, 0, 0), 5) #เส้นสีแดง หนา 5 พิกเซล45องศา
#or arrowedLine , circle , rectangle , putText
cv2.imshow("Line", imgresize)
cv2.waitKey(0)  
cv2.destroyAllWindows()
