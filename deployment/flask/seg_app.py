import base64
import numpy as np
import io
import datetime
import pymongo
from PIL import Image
import tensorflow as tf
from tensorflow.python.keras import backend as K 
from tensorflow.python.keras import models
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import Flask, jsonify, request
#import cv2

app =Flask('__name__')

def connect_db():
	client =pymongo.MongoClient('mongodb://172.17.0.2:27017/')
	db =client["seg_logs_db"]
	col =db['logs']
	print(client.list_database_names())

	return col

def get_model():
	global model
	global graph
	# model =models.load_model('/Users/anass/flask_test/models/weights_sigmoid_mse_loss.hdf5')
	model =models.load_model('/app/models/weights_sigmoid_mse_loss.hdf5')
	model._make_predict_function()
	graph = tf.get_default_graph()

	print('model loaded')

def preproc_func(img, size):
	img =img.resize(size)
	img =img_to_array(img)*1/255.
	img =np.expand_dims(img, axis=0)

	return img

print ('loading model....')
get_model()
col =connect_db()
print('go to http://localhost:5000/static/segment.html')

@app.route('/segment', methods=['POST'])
def segment():
	print(request.remote_addr, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.method, request.url)

	message =request.get_json(force=True)
	encoded =message['img']
	decoded =base64.b64decode(encoded)
	img =Image.open(io.BytesIO(decoded))
	preproc_img =preproc_func(img, (256, 256))

	doc ={'ip': request.remote_addr, 'datetime':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'request':'%s %s'%(request.method, request.url), 'img': encoded}
	x =col.insert_one(doc)
		
	global graph
	with graph.as_default():
		pred_mask =model.predict(preproc_img, steps=1)[0]*255

	#cv2.imwrite('/Users/anass/flask_test/test_mask.JPG', pred_mask)
	print(pred_mask.shape)
	mask_list =pred_mask.tolist()
	print(mask_list[0][1][2])

	#responce ={'mask': 'test_mask.JPG'}
	responce ={'mask': mask_list}

	return jsonify(responce)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

