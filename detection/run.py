import io
import os
from PIL import Image
import cv2
import numpy as np
from base64 import b64decode, b64encode
from .utils import *
from .darknet import Darknet
import cv2
import matplotlib.pyplot as plt
import uuid
try:
    #load model for Screwdata format
    #cfg_file = './cfg/yolov3-Screwdata.cfg'
    cfg_file = './detection/cfg/yolov3-Screwdata.cfg'
    weight_file = './detection/weights/yolov3-Screwdata_final.weights'
    namesfile = './detection/data/Screw_data.names'
    
except:
    print('Path is Error!!!')

def load_model():
    global m
    global class_names
    m = Darknet(cfg_file)
    m.load_weights(weight_file)
    class_names = load_class_names(namesfile)
    return {'status': 'yolov3 is ready'}


def inferenceYoLo(original_image):
    m = Darknet(cfg_file)
    m.load_weights(weight_file)
    class_names = load_class_names(namesfile)

    original_image = np.array(original_image).astype('uint8')
    resized_image = cv2.resize(original_image, (m.width, m.height), interpolation=cv2.INTER_AREA)

    nms_thresh = 0.4
    iou_thresh = 0.6
    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)
    url = plot_boxes(original_image, boxes, class_names, plot_labels=True)
    objects = print_objects(boxes, class_names)
    plt.imshow(original_image)
    name = os.path.join('./images', str(uuid.uuid1()) + '.png')
    im = plt.savefig(name)
    return {'objects': objects}

