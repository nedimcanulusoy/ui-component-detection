from PIL import Image
from flask import Flask, request, jsonify
from ultralytics import YOLO

#Load the YOLOv5 model with your pre-trained weights
path_ = 'runs/train/weights/best.pt'
model = YOLO(path_)

#Set up the Flask app
app = Flask(__name__)

#Define the route for the API
@app.route('/api/predict', methods=['POST', 'GET'])
def predict():
    #Get the image file from the request
    image_file = request.files['image']

    #Load the image and make predictions using the YOLOv5 model
    image = Image.open(image_file)
    result = model.predict(source=image, save=True)

    #Return the predictions as a JSON response
    return jsonify(result.pandas().to_dict())

if __name__ == '__main__':
    app.run(debug=True)
