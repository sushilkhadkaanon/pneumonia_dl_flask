

import uvicorn
from keras.models import model_from_json
from flask import Flask, render_template, request
import numpy as np
import os

from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image





app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/')
def index_view():
    return render_template('index.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        img = image.load_img(file_path, target_size=(100, 100))
        img_array = image.img_to_array(img)
        img_batch = np.expand_dims(img_array, axis=0)
        json_file = open('model/model.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        

        loaded_model.load_weights("model/model.h5")
        print("Loaded Model from disk")

        predict = loaded_model.predict(img_batch)
        
        
        if predict[0][0]>predict[0][1]: 
            result = "NORMAL" 
            accuracy = predict[0][0]
        else: 
            result = "PNEUMONIA" 
            accuracy = predict[0][1]
        
        return render_template('predict.html', result=result,file_path=file_path,accuracy = accuracy)
        



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
