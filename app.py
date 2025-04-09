from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load the trained model and label encoder
model = joblib.load('random_forest_model.pkl')
le = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input features from the form
        features = np.array([[
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]])

        # Make prediction using the model
        prediction = model.predict(features)
        recommended_crop = le.inverse_transform(prediction)[0]

        # Get growing tips for the predicted crop
        growing_tips = get_growing_tips(recommended_crop)

        # Get image path for the predicted crop
        crop_image = get_crop_image(recommended_crop)

        # Render the result page with the predicted crop, growing tips, and image path
        return render_template('result.html', crop=recommended_crop, growing_tips=growing_tips, crop_image=crop_image)
    except Exception as e:
        return render_template('index.html', error=str(e))

def get_growing_tips(crop):
    tips = {
        'rice': "Rice grows best in hot and humid climates. It needs plenty of water and is often grown in flooded fields called paddies.",
        'maize': "Maize is grown in warm climates and prefers well-drained soil. Ensure regular watering and remove weeds for better yield.",
        'chickpea': "Chickpeas thrive in dry climates. They need moderate watering and should be grown in well-drained soil with good sunlight.",
        'kidney beans': "Kidney beans require well-drained, nutrient-rich soil. Ensure the soil is moist, but not waterlogged.",
        'pigeon peas': "Pigeon peas grow well in tropical climates. They require minimal water and can be grown in a variety of soils.",
        'mothbeans': "Mothbeans are drought-resistant and thrive in dry, sandy soils. They require very little water and care.",
        'mungbean': "Mungbean prefers warm temperatures and well-drained soil. Regular watering is essential for a healthy yield.",
        'blackgram': "Blackgram grows well in warm, humid conditions. It requires well-drained soil and consistent moisture.",
        'lentil': "Lentils prefer cool climates and are drought-tolerant. They need minimal watering once established.",
        'pomegranate': "Pomegranates thrive in hot, dry climates and well-drained soil. They require little water once established.",
        'banana': "Bananas grow best in tropical climates with plenty of water. They need rich, well-drained soil and regular fertilization.",
        'mango': "Mango trees require hot temperatures and well-drained soil. Ensure regular watering and proper pruning for the best yield.",
        'grapes': "Grapes prefer warm climates and well-drained soil. They need full sun exposure and regular pruning to maximize growth.",
        'watermelon': "Watermelons need warm weather and plenty of space. Plant them in sandy, well-drained soil with regular watering.",
        'muskmelon': "Muskmelon grows best in sandy, well-drained soil. It needs full sunlight and frequent watering during the growing season.",
        'apple': "Apple trees prefer cool climates and well-drained soil. Regular pruning and pest management are important for healthy growth.",
        'orange': "Oranges thrive in warm, subtropical climates with well-drained soil. They require regular watering and fertilization.",
        'papaya': "Papayas prefer warm, tropical climates and well-drained soil. They need regular watering and fertilization to grow well.",
        'coconut': "Coconuts grow in tropical, coastal regions. They need sandy, well-drained soil and plenty of sunlight.",
        'cotton': "Cotton requires a long, warm growing season. Plant it in fertile, well-drained soil and ensure regular watering.",
        'jute': "Jute grows best in hot, humid climates. It needs heavy rainfall and is often grown near rivers or areas with rich soil.",
        'coffee': "Coffee plants prefer tropical climates and well-drained soil. They need shade and regular watering for optimal growth."
    }
    return tips.get(crop.lower(), 'No specific growing tips available for this crop.')

def get_crop_image(crop):
    # Dictionary mapping crops to image filenames
    images = {
        'rice': 'rice.jpeg',
        'maize': 'maize.jpeg',
        'chickpea': 'chickpea.jpeg',
        'kidney beans': 'kidney_beans.jpeg',
        'pomegranate': 'pomegranate.jpeg',
        'banana': 'banana.jpeg',
        'mango': 'mango.jpg',
        'grapes': 'grapes.jpg',
        'apple': 'apple.jpg',
        'orange': 'orange.jpg',
        'coffee': 'coffee.jpg',
        'watermelon': 'watermelon.jpg',
        'cotton': 'cotton.jpg',
        # Add other crops and their images here...
    }
    return f"static/images/{images.get(crop.lower(), 'default.jpg')}"

if __name__ == '__main__':
    app.run(debug=True)
