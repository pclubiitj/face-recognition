import numpy as np
import matplotlib.pyplot as plt
import cv2
import torch
from util.face_detection.face_ssd_infer import SSD
from util.face_detection.utils import vis_detections
import os
import sys
from tqdm import tqdm


def extractor(img_path, device="cuda", conf_thresh=0.1, target_size=(576, 576), path='face_extractor/face_detection/weights/WIDERFace_DSFD_RES152.pth'):

    device = torch.device(device)
    net = SSD("test")
    net.load_state_dict(torch.load(path))
    net.to(device).eval()
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    # target_size = img.shape[:-1]
    # print(target_size)
    detections = net.detect_on_image(
        img, target_size, device, is_pad=False, keep_thresh=conf_thresh)
    bbox_list = vis_detections(
        img, detections, conf_thresh)  # , show_text=False  # x1,y1,x2,y2

    return bbox_list, img, target_size


# bbox_list, img, target_size = face_detection('ignus.JPG')
# bbox_list = np.int32(bbox_list)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# for i in range(len(bbox_list)):
#     img = cv2.rectangle(img, (bbox_list[i][0], bbox_list[i][1]),
#                         (bbox_list[i][2], bbox_list[i][3]), (0, 255, 0), 7)
# img = cv2.imread('ignus.JPG')
# print(bbox_list)
# print(len(bbox_list))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imwrite('output.jpg', img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# plt.imshow(img)
# plt.show()
