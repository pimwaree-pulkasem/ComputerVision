import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #เฟมเรต ขนาดวิดีโอ

while (cap.isOpened()):
    check, frame = cap.read()
    if not check:
        break
    currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #ดึงเวลาปัจจุบันของวิดีโอ
    cv2.putText(frame, "Time: " + currentDateTime, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,0),5)
    cv2.imshow('Camera', frame)
    output.write(frame) #บันทึกวิดีโอ
    if cv2.waitKey(1) & 0xFF == ord('e') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
        break
output.release() #ปิดการบันทึกวิดีโอ
cap.release()
cv2.destroyAllWindows()  


