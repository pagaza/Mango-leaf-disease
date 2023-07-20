#!/usr/bin/python3

import jetson_inference
import jetson_utils
from jetson_inference import imageNet

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
opt = parser.parse_args()

img = jetson_utils.loadImage(opt.filename)

net = imageNet(model="models/resnet18.onnx", labels="models/labels.txt", 
                 input_blob="input_0", output_blob="output_0")

class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idx)

#return image w class and confidence overlay as output

print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))  