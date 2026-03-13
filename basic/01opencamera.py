import cv2
cap = cv2.VideoCapture(0)
while (True):
    check, frame = cap.read()
    if not check:
        break
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('e') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
cv2.destroyAllWindows()  

