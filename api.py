import flask
import tensorflow as tf
from PIL import Image
import keras
from keras.models import load_model

app = flask.Flask(__name__)

model = load_model('gartic.hdf5')

@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.data

    if (params != None):
        np_img = np.array(params, dtype='uint8')
        data["prediction"] = str(model.predict(np_img)[0][0])
        data["success"] = True

    return flask.jsonify(data)    

app.run(host='0.0.0.0', port=5000)