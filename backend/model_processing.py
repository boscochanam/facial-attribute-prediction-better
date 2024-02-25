import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
import cv2
from skimage import io
from PIL import Image
import json


def predict_attributes(file_path):
    # Load the model from the specified directory
    model_path = r'C:\Users\chana\Documents\Coding\Flexi Mobile\facial-attribute-prediction\backend\models\mirrored-tts-rnt101-a1g3e70.h5'  # Replace with the correct path
    model = tf.keras.models.load_model(model_path)

    # Define the preprocessing function
    def load_and_preprocess_image(file_path):
        # Load the image and resize it
        image = Image.open(file_path)

        # Resize the image to (224, 224) for model input
        image = image.resize((224, 224))

        return image

    # Load and preprocess the image
    img = load_and_preprocess_image(file_path)

    # Load the image using OpenCV for face detection
    image_cv2 = cv2.imread(file_path)

    # Use a pre-trained face detection model to find faces in the image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    # Crop the detected face(s) and preprocess for prediction
    for (x, y, w, h) in faces:
        # Crop the detected face
        cropped_face = image_cv2[y:y+h, x:x+w]

        # Create an image object from the cropped face
        cropped_face_img = Image.fromarray(cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB))

        # Resize the cropped face to (224, 224) for model input
        cropped_face_img = cropped_face_img.resize((224, 224))

        # Make predictions on the cropped face
        cropped_face_array = np.array(cropped_face_img)
        cropped_face_array = cropped_face_array[None, ...]  # Add batch dimension
        age_prediction, gender_prediction, ethnicity_prediction = model.predict(preprocess_input(cropped_face_array))

        # Post-process the predictions if needed
        # For example, you can convert gender_prediction to 'Male' or 'Female' based on a threshold

        # Store the predictions for the cropped face
        result = {
            'Age': int(age_prediction[0][0]),  # Convert age_prediction to int
            'Gender': 'Female' if gender_prediction[0] > 0.1 else 'Male',
            'Ethnicity': {
                'White': int(ethnicity_prediction[0][0]*100),
                'Black': int(ethnicity_prediction[0][1]*100),
                'Asian': int(ethnicity_prediction[0][2]*100),
                'Brown': int(ethnicity_prediction[0][3]*100),
                'Other Brown': int(ethnicity_prediction[0][4]*100)
            }
        }

    # Return the results as JSON
    print(result)
    return result
