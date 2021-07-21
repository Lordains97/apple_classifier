import os
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

model = load_model('/content/drive/MyDrive/apple_classifier_model')

def predictImage(filename):
    img1 = image.load_img(filename,target_size=(200,200))
    Y = image.img_to_array(img1)
    X = np.expand_dims(Y,axis=0)
    val = model.predict(X)
    print(val)
    if val == 1:
        print(filename+" = Not an apple")
    elif val == 0:
        print(filename+" = An apple")

f = r'/content/test'
for file in os.listdir(f):
    img = f+"/"+file
    predictImage(img)

