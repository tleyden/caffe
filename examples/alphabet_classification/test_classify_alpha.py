
'''
Before running this, you may need to run:

export PYTHONPATH=/opt/caffe/python

Also you will need to create an IMAGE_FILE in the current directory

'''

import numpy as np
caffe_root = '../'
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

MODEL_FILE = 'alpha_classifier.prototxt'
PRETRAINED = 'alpha_iter_1300.caffemodel'
IMAGE_FILE = '6.png'

net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       raw_scale=255,
                       image_dims=(28, 28))

net.set_phase_test()
net.set_mode_cpu()

input_image = caffe.io.load_image(IMAGE_FILE, color=False)

prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
print 'prediction shape:', prediction[0].shape
print 'predicted class:', prediction[0].argmax()
