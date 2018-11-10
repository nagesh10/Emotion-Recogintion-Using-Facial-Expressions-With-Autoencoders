#-------------------------------------------------------------------------------
# Name:        EmotionDetectionUsingFacialExpressionsWithAutoencoders
# Purpose:
#
# Author:      sivaprasadrb
#
# Created:     10/11/2018
# Copyright:   (c) sivaprasadrb 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from __future__ import print_function
import keras
import os
from keras.layers import Input,Conv2D, MaxPooling2D, UpSampling2D,  Dense
from keras.models import Model
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras import optimizers

import numpy as np
import matplotlib.pyplot as plt

data_path = './data/'

imgs = np.empty((256, 256), int)

filenames = sorted(os.listdir(data_path))
classificationLabels = []
count = 0
for img_name in filenames:
    img = plt.imread(data_path + img_name)
    img  = np.resize(img, (256, 256))
    if count == 0:
	imgs=(img)
	count = 1
    else:
    	imgs = np.append(imgs, img, axis=0)
    classificationLabels.append(int(img_name[1]))

imgs = np.reshape(imgs, [213, 256, 256])
print(imgs.shape)

train_images, test_images, train_labels, test_labels = train_test_split(imgs, d, test_size=0.33, random_state=42)

from keras.utils import to_categorical


print('Training data shape : ', train_images.shape, len(train_labels))

print('Testing data shape : ', test_images.shape, len(test_labels))

classes = np.unique(train_labels)

classes=np.append(classes,0)
nClasses = len(classes)

print('Total number of outputs : ', nClasses)
print('Output classes : ', classes)

plt.figure(figsize=[4,2])

plt.subplot(121)
plt.imshow(train_images[0,:,:], cmap='gray')
plt.title("Ground Truth : {}".format(train_labels[0]))

plt.subplot(122)
plt.imshow(test_images[0,:,:], cmap='gray')
plt.title("Ground Truth : {}".format(test_labels[0]))