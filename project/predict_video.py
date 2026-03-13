import cv2
from ultralytics import YOLO

model = YOLO('C:/ComputerVision/project/train3/weights/best.pt') 

video_path = 'video/Orange.mp4' 
cap = cv2.VideoCapture(video_path)

cv2.namedWindow("YOLOv8 Fruit QC Inspection")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
    results = model.predict(frame, conf=0.5, verbose=False) 
    annotated_frame = results[0].plot()
    
    cv2.imshow("YOLOv8 Fruit QC Inspection", annotated_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
        
  
    if cv2.getWindowProperty("YOLOv8 Fruit QC Inspection", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
