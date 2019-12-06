import tensorflow as tf 
import keras
import cv2
import numpy as np

import base64
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}
    img = request.get_json()
    starter = img.find(',')
    image_data = img[starter+1:]
    decoded = base64.b64decode(image_data)

    with open('image.jpg', 'wb') as fh:
        fh.write(decoded)
        fh.close()
    data["success"] = True
    classifierLoad = tf.keras.models.load_model('gartic.hdf5') 
    image = cv2.imread('image.jpg')
    small_image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_CUBIC)
    small_image, _, _ = cv2.split(small_image)
    data['index'] = (classifierLoad.predict_classes(np.expand_dims([small_image], axis=-1)).tolist()[0])


    return jsonify(data)    

app.run(host='0.0.0.0', port=5000)