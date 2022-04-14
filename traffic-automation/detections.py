import cv2
import numpy as np

def findObjects(outputs, img, confThreshold, nmsThreshold, classNames, count, use, useable):
    hT, wT, CT = img.shape 
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2]*wT), int(det[3]*hT)
                x, y = int((det[0] * wT) - w/2), int((det[1]*hT) - h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        
        box = bbox[i]
        x,y,w,h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0),2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%', (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

        count += 1
        if classNames[classIds[i]].upper() in useable:
            use += 1
    return [count,use]

def initialize(inputImg):
    whT = 320
    confThreshold = 0.1
    nmsThreshold = 0.3
    count = 0
    use = 0
    useable = ["PERSON", "BICYCLE", "CAR", "MOTORBIKE", "BUS", "TRUCK"]

    classesFile = r"E:\workspace\coco.names"
    classNames = []
    with open(classesFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    modelConfiguration = r"E:\workspace\yolov3.cfg"
    modelWeights = r"E:\workspace\yolov3.weights"
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    img = cv2.cvtColor(inputImg, cv2.COLOR_RGB2BGR)

    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop = False)
    net.setInput(blob)
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)

    data = findObjects(outputs, img, confThreshold, nmsThreshold, classNames, count, use, useable)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return data