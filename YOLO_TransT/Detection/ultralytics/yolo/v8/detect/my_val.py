##val
from ultralytics.yolo.engine.model import YOLO
if __name__=="__main__":
    model=YOLO("")      #Path of detecting weight 
    model.val(data="",name="")    #Path of data configuration file 
