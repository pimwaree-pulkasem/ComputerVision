import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #เฟมเรต ขนาดวิดีโอ

while (cap.isOpened()):
    check, frame = cap.read()
    if not check:
        break
    cv2.imshow('Camera', frame)
    output.write(frame) #บันทึกวิดีโอ
    if cv2.waitKey(1) & 0xFF == ord('e') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
        break
output.release() #ปิดการบันทึกวิดีโอ
cap.release()
cv2.destroyAllWindows()  

