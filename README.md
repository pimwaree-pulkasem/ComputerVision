folder : project
Fruit Quality Control Inspection (YOLOv8)

ฟีเจอร์หลัก (Key Features)
Real-time Detection: ตรวจจับผลไม้ประเภทต่างๆ (ส้ม, แอปเปิ้ล, กล้วย , แครอท) จากวิดีโอ

Quality Classification: จำแนกเกรดของผลไม้เบื้องต้น (เช่น ผลผลิตสมบูรณ์ / ผลผลิตที่มีตำหนิ) //เนื่องจากตัว dataset ไม่มี label แยกผลที่มีตำหนิ จึงเป็นส่วนที่ต้องปรับปรุง

YOLOv8 Implementation: ใช้โมเดล Ultralytics YOLOv8 

เครื่องมือที่ใช้ (Tech Stack)
Language: Python 3.11

Library: OpenCV, Ultralytics (YOLOv8)

Dataset: ฝึกฝนโมเดลด้วย Dataset จาก Roboflow
https://universe.roboflow.com/fruits-dataset/fruitsv2-duplk

สิ่งที่กำลังพัฒนาและแผนในอนาคต (Roadmap & Future Improvements)
มีแผนที่จะปรับปรุงโปรเจกต์นี้ให้มีประสิทธิภาพมากขึ้นในอนาคต ดังนี้:
- ปรับแต่งโมเดล (Fine-tuning) ให้มีความแม่นยำสูงขึ้นในสภาวะแสงที่แตกต่างกัน
- เพิ่มจำนวน dataset ให้ครอบคลุมมากขึ้น

ผลการทดลองหรือกราฟ (Training Results) https://github.com/pimwaree-pulkasem/ComputerVision/tree/main/project/train3

วิดีโอผลการรัน https://1drv.ms/f/c/055dbb0a89a31fa1/IgB_n_e4O6HSTZuD_YY3LWRFAVMtfCSZqxp4HwQVrhkRiqk?e=IH3jt5
