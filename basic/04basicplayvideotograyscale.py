import cv2
cap = cv2.VideoCapture("image/video.MOV")
cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camera', 800, 500)

while (cap.isOpened()):
    check, frame = cap.read()
    if not check:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Camera', gray)
    if cv2.waitKey(1) & 0xFF == ord('e') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
        break
cap.release()
cv2.destroyAllWindows()  

