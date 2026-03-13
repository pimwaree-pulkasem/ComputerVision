import cv2
import numpy
image = numpy.zerps([400,400,3])
img = cv2.imread("image/shutterstock_669619393.jpg")
def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (100, 100), (800, 500), (255, 0, 0), 5)
      
cv2.imshow("Image", img)
cv2.setMouseCallback("Image",clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()