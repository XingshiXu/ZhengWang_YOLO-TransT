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

sys.path.append(' ')  #Add Path
import cv2
import torch
import numpy as np
from glob import glob
from pysot_toolkit.bbox import get_axis_aligned_bbox
from pysot_toolkit.trackers.tracker import Tracker
from pysot_toolkit.trackers.net_wrappers import NetWithBackbone

from ultralytics.yolo.engine.model import YOLO
if __name__=="__main__":
    model=YOLO(" ")             #Path of detecting weight 
    model.predict(
                  source=" ",                                      #Path of test video
                  conf=0.7,
                  save_txt=True,
                  save=True
                  )

init_bbox = None
