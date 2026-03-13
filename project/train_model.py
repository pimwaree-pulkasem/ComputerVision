from ultralytics import YOLO

def train():

    model = YOLO('yolov8n.pt') 

    model.train(
        data='C:/ComputerVision/project/Fruitsv2.v5i.yolov8/data.yaml', 
        epochs=50,
        imgsz=640,
        device=0,   
        workers=2      
    )

if __name__ == '__main__':
    train()