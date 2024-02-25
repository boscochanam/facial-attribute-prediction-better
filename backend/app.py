import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import matplotlib.pyplot as plt
from model_processing import predict_attributes
from flask import request

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/time')
def time():
    x = datetime.datetime.now()
    return jsonify({
        "time": x
    })


@app.route('/pic-send', methods=['POST'])
def pic_send():
    # Check if 'image' exists in request.files
    if 'image' not in request.files:
        return {"message": "Not Found Sorry"}

    # Get the file object from the request
    image_file = request.files['image']

    # Save the image to a file (you can save it to any desired location)
    image_file.save('uploaded_image.jpg')

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the local path relative to the current directory
    local_path = os.path.join(current_dir, 'uploaded_image.jpg')
    data = predict_attributes(local_path)

    os.remove(local_path)

    # Return a response to the client
    return data


CORS(app)
# Running app
if __name__ == '__main__':
    app.run(debug=True)
