##train
from ultralytics.yolo.engine.model import YOLO

if __name__=="__main__":
    model=YOLO("")
    model.train(
        data="",
        epochs=300,
        imgsz=640,
        batch=32,
        workers=16,
        device=0,
        patience=300,  # epochs to wait for no observable improvement for early stopping of training
        save=True,  # save train checkpoints and predict results
        save_period=-1,  # Save checkpoint every x epochs (disabled if < 1)
        cache=False,  # True/ram, disk or False. Use cache for data loading
        pretrained=True,  # whether to use a pretrained model
        resume=True,  # resume training from last checkpoint
        amp=True  # Automatic Mixed Precision (AMP) training, choices=[True, False], True runs AMP check
    )
    model.train(**{'cfg': 'ultralytics/yolo/cfg/default.yaml'})