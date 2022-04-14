import cv2
import numpy as np
import detections as det

def region(img, vertices):
    mask = np.zeros_like(img) 
    channelCount = img.shape[2]
    matchMaskColor = (255,)*channelCount 
    cv2.fillPoly(mask, vertices, matchMaskColor)
    maskedImg = cv2.bitwise_and(img, mask)
    maskedImg = cv2.cvtColor(maskedImg, cv2.COLOR_RGB2BGR)
    return maskedImg


def initialize(srcPath):
    img = cv2.imread(srcPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height = img.shape[0]
    width = img.shape[1]
    regionVertices = [(40,height), (width/2.5, height/20), (800, height/20),(width, height)]
    cropped = region(img, np.array([regionVertices], np.int32))
    data = det.initialize(cropped)
    return data