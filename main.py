from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load models
model_v1 = load_model('models/model_v1.keras')
model_v2 = load_model('models/model_v2.keras')
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

# Route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get image from request
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    # Preprocess image
    image = np.array(image)
    # Make predictions using both models
    prediction_v1 = model_v1.predict(np.expand_dims(image, axis=0))
    prediction_v2 = model_v2.predict(np.expand_dims(image, axis=0))
    prediction_class_v1 = CLASS_NAMES[np.argmax(prediction_v1)]
    prediction_class_v2 = CLASS_NAMES[np.argmax(prediction_v2)]
    # Return predictions as JSON response
    return jsonify({
        'prediction_v1': prediction_class_v1,
        'prediction_v2': prediction_class_v2
    })


if __name__ == '__main__':
    app.run(debug=True)
