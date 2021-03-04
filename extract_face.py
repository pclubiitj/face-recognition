import os
import cv2
import argparse
import numpy as np
# from database import match
import matplotlib.pyplot as plt
from tqdm.autonotebook import tqdm
from face_extractor.utils import extractor


def extract_landmark(path, folder_path, file):
    bbox_list, img, _ = extractor(path, conf_thresh=0.3)  # x1,y1,x2,y2
    count = 0
    # Extracted Face Files: list of files corresponding to extracted faces from the image
    extr_face_files = list()

    if bbox_list != None:
        for i in bbox_list:
            i = np.int32(i)
            if i[0] > 0 and i[1] > 0 and i[2] > 0 and i[3] > 0:
                count += 1
                file_path = (os.path.splitext(path)[
                             0]+'_{}.jpg'.format(count)).replace(folder_path, folder_path+'_face')
                crop_img = img[i[1]:i[3], i[0]:i[2]]
                cv2.imwrite(file_path, crop_img)
                file.write(path+'|'+file_path+'\n')
                # match(path, file_path)
                # extr_face_files.append(file_path)
        # return extr_face_files


if __name__ == '__main__':

    folder_path = 'folder'
    os.makedirs('extracted_face/'+folder_path+'_face', exist_ok=True)
    image_list = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        image_list.append(file_path)

    file = open('metadata.txt', 'a')
    for path in tqdm(image_list, total=len(image_list)):
        extract_landmark(path, folder_path, file)
    file.close()
