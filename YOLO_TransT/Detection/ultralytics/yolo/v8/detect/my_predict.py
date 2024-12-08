##val
# 跟踪
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals



import os
import sys
env_path = os.path.join(os.path.dirname(__file__), '..')
print(env_path)
if env_path not in sys.path:
    sys.path.append(env_path)
import argparse
import os


sys.path.append('/home/test/wz/TransT')  # 添加到python的搜索路径
import cv2
import torch
import numpy as np
from glob import glob
from pysot_toolkit.bbox import get_axis_aligned_bbox
from pysot_toolkit.trackers.tracker import Tracker
from pysot_toolkit.trackers.net_wrappers import NetWithBackbone

from ultralytics.yolo.engine.model import YOLO
if __name__=="__main__":
    model=YOLO("/media/test/WZ/02_YOLOv8_Transt/yolov8_transt/yolov8/ultralytics/yolo/v8/detect/best.pt")
    model.predict(
                  source="/media/test/WZ/02_YOLOv8_Transt/dataset/1/video/00097.mp4",                                      #test video
                  conf=0.7,
                  save_txt=True,
                  save=True
                  )

init_bbox = None