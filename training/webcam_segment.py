import cv2 
import numpy as np
import tensorflow as tf
from tensorflow.python.keras import models

def get_model():
    global model
    global graph
    model =models.load_model('/Users/anass/flask_test/models/weights_sigmoid_mse_loss.hdf5')
    model._make_predict_function()
    graph = tf.get_default_graph()

    print('model loaded')

def preproc_func(img, size):
    resized_img =cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    preproc_img =np.expand_dims(resized_img, axis=0)*1/255.

    return preproc_img

print ('loading model....')
get_model()

cap =cv2.VideoCapture(0)

while True:
    ret, img =cap.read()
    preproc_img =preproc_func(img[:,280:1000,:], (256, 256))
    print(preproc_img[0].shape)

    global graph
    with graph.as_default():
        pred_mask =model.predict(preproc_img, steps=1)[0]
          
    cv2.imshow('preproc_img', preproc_img[0])        
    cv2.imshow('mask', pred_mask)
    
    k =cv2.waitKey(27) &0xFF
    if k ==27:
        break
    
cap.release()
cv2.destroyAllWindows()