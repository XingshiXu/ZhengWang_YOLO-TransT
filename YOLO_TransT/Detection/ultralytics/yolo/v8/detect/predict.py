# Ultralytics YOLO 🚀, AGPL-3.0 license

import torch

from ultralytics.yolo.engine.predictor import BasePredictor
from ultralytics.yolo.engine.results import Results
from ultralytics.yolo.utils import DEFAULT_CFG, ROOT, ops


# add track


import os
import sys
env_path = os.path.join(os.path.dirname(__file__), '..')
print(env_path)
if env_path not in sys.path:
    sys.path.append(env_path)
import argparse
import os

sys.path.append('') 
import cv2
import torch
import numpy as np
from glob import glob

# from pysot.core.config import cfg
# from pysot.models.model_builder import ModelBuilder
# from pysot.tracker.tracker_builder import build_tracker
# python tools/demo.py --config experiments/siamrpn_r50_l234_dwxcorr/config.yaml --snapshot experiments/siamrpn_r50_
# l234_dwxcorr/model.pth --video demo/bag.avi

from pysot_toolkit.bbox import get_axis_aligned_bbox
# from pysot_toolkit.toolkit.datasets import DatasetFactory
# from pysot_toolkit.toolkit.utils.region import vot_overlap, vot_float2str
from pysot_toolkit.trackers.tracker import Tracker
from pysot_toolkit.trackers.net_wrappers import NetWithBackbone


class DetectionPredictor(BasePredictor):

    def preprocess(self, img):
        """Convert an image to PyTorch tensor and normalize pixel values."""
        img = (img if isinstance(img, torch.Tensor) else torch.from_numpy(img)).to(self.model.device)
        img = img.half() if self.model.fp16 else img.float()  # uint8 to fp16/32
        img /= 255  # 0 - 255 to 0.0 - 1.0
        return img

    def postprocess(self, preds, img, orig_imgs):
        """Postprocesses predictions and returns a list of Results objects."""
        preds = ops.non_max_suppression(preds,
                                        self.args.conf,
                                        self.args.iou,
                                        agnostic=self.args.agnostic_nms,
                                        max_det=self.args.max_det,
                                        classes=self.args.classes)

        results = []

        # transT
        first_frame = True
        count = 1  
        current_frame_num = 0

        boxes = []
        for i, pred in enumerate(preds):
            orig_img = orig_imgs[i] if isinstance(orig_imgs, list) else orig_imgs
            if not isinstance(orig_imgs, torch.Tensor):
                pred[:, :4] = ops.scale_boxes(img.shape[2:], pred[:, :4], orig_img.shape)
                # coor
                # print(f'pred = {pred[:, :4]}')
            path, _, _, _, _ = self.batch
            img_path = path[i] if isinstance(path, list) else path
            # print(f'self.model.names = {self.model.names}')
            results.append(Results(orig_img=orig_img, path=img_path, names=self.model.names, boxes=pred))
        return results


def predict(cfg=DEFAULT_CFG, use_python=False):
    """Runs YOLO model inference on input image(s)."""
    model = cfg.model or 'yolov8n.pt'
    source = cfg.source if cfg.source is not None else ROOT / 'assets' if (ROOT / 'assets').exists() \
        else 'https://ultralytics.com/images/bus.jpg'

    args = dict(model=model, source=source)
    if use_python:
        from ultralytics import YOLO
        YOLO(model)(**args)
    else:
        predictor = DetectionPredictor(overrides=args)
        predictor.predict_cli()



if __name__ == '__main__':
    predict()
