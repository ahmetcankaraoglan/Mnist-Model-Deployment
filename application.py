from flask import Flask, render_template, request, make_response
from flask_cors import CORS, cross_origin
import base64
import io
from PIL import Image
import numpy as np
import json



app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/send_image', methods=['POST'])
@cross_origin()
def send_image():
    data = request.form.get('send')
    data = data.split(',')[1]
    im = base64.b64decode(data)
    buf = io.BytesIO(im)
    img = Image.open(buf)
    img = img.resize((28, 28), Image.ANTIALIAS)
    image_data = np.array(list(img.getdata()))[:, -1].reshape(28, 28)
    image_data = image_data/max(image_data.ravel())

    image_data = image_data.reshape(1, 28, 28, 1)
    return json.dumps({"image": image_data.tolist()})

if __name__=='__main__':
    app.run()

