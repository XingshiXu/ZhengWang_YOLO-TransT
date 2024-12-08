##val
from ultralytics.yolo.engine.model import YOLO
if __name__=="__main__":
    model=YOLO("/media/test/249C3D769C3D4418/wz/yolov8/ultralytics/yolo/v8/detect/runs/detect/yolov8n_NWD/weights/best.pt")
    model.val(data="/media/test/249C3D769C3D4418/wz/yolov8/ultralytics/datasets/coco128.yaml",name="yyyy")