# Copyright (c) SenseTime. All Rights Reserved.

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

import cv2
import torch
import numpy as np
from glob import glob
from pysot_toolkit.bbox import get_axis_aligned_bbox
# from pysot_toolkit.toolkit.datasets import DatasetFactory
# from pysot_toolkit.toolkit.utils.region import vot_overlap, vot_float2str
from pysot_toolkit.trackers.tracker import Tracker
from pysot_toolkit.trackers.net_wrappers import NetWithBackbone

parser = argparse.ArgumentParser(description='transt tracking')
parser.add_argument('--dataset', default='OTB2015',type=str,
        help='datasets')
parser.add_argument('--video', default='', type=str,
        help='eval one special video')
parser.add_argument('--vis', default='',action='store_false',
        help='whether visualzie result')
parser.add_argument('--name', default='', type=str,
        help='name of results')
args = parser.parse_args()

torch.set_num_threads(1)


def get_frames(video_name):
    if not video_name:
        cap = cv2.VideoCapture(0)
        # warmup
        for i in range(5):
            cap.read()
        while True:
            ret, frame = cap.read()
            if ret:
                yield frame
            else:
                break
    elif video_name.endswith('avi') or \
        video_name.endswith('mp4'):
        cap = cv2.VideoCapture(video_name)
        while True:
            ret, frame = cap.read()
            if ret:
                yield frame
            else:
                break
    else:
        images = glob(os.path.join(video_name, '*.jp*'))
        images = sorted(images,
                        key=lambda x: int(x.split('/')[-1].split('.')[0]))
        for img in images:
            frame = cv2.imread(img)
            yield frame

def main():
    # load config

    #dataset_root = r'/home/test/wz/dataset/OTB2015/' #Absolute path of the dataset
    net_path = r'/media/test/WZ/02_YOLOv8_Transt/yolov8_transt/TransT/ltr/checkpoints/checkpoints_official/transt_N2.pth' #Absolute path of the model

    # create model
    net = NetWithBackbone(net_path=net_path, use_gpu=True)
    tracker = Tracker(name='transt', net=net, window_penalty=0.49, exemplar_size=128, instance_size=256)

    # create dataset
    model_name = args.name
    toc = 0
    pred_bboxes = []
    scores = []
    track_times = []
    video = '/media/test/WZ/02_YOLOv8_Transt/yolov8_transt/00100.mp4'
    idx = 0
    for img in get_frames(video):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        tic = cv2.getTickCount()
        if idx == 0:
            try:
                init_rect = cv2.selectROI(video, img, False, False)
            except:
                exit()
            gt_bbox_ = init_rect
            init_info = {'init_bbox':gt_bbox_}
            tracker.initialize(img, init_info)
            pred_bbox = gt_bbox_
            scores.append(None)
            pred_bboxes.append(pred_bbox)
        else:
            outputs = tracker.track(img)
            pred_bbox = outputs['target_bbox']
            pred_bboxes.append(pred_bbox)
            scores.append(outputs['best_score'])
        toc += cv2.getTickCount() - tic
        track_times.append((cv2.getTickCount() - tic)/cv2.getTickFrequency())
        if idx == 0:
            cv2.destroyAllWindows()
        if idx > 0:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # gt_bbox = list(map(int, gt_bbox))
            pred_bbox = list(map(int, pred_bbox))
            # cv2.rectangle(img, (gt_bbox[0], gt_bbox[1]),
            #               (gt_bbox[0]+gt_bbox[2], gt_bbox[1]+gt_bbox[3]), (0, 255, 0), 3)
            cv2.rectangle(img, (pred_bbox[0], pred_bbox[1]),
                          (pred_bbox[0]+pred_bbox[2], pred_bbox[1]+pred_bbox[3]), (0, 255, 255), 3)
            cv2.putText(img, str(idx), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow(video, img)
            cv2.waitKey(1)
        idx += 1
    toc /= cv2.getTickFrequency()
    # save results
    model_path = os.path.join('results', model_name)
    if not os.path.isdir(model_path):
        os.makedirs(model_path)
    result_path = os.path.join(model_path, '{}.txt'.format(video))
    with open(result_path, 'w') as f:
        for x in pred_bboxes:
            f.write(','.join([str(i) for i in x])+'\n')
    print('Video: {:12s} Time: {:5.1f}s Speed: {:3.1f}fps'.format(
        video, toc, idx / toc))


if __name__ == '__main__':
    main()
