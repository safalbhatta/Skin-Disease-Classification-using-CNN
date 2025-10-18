from django.shortcuts import render
from PIL import Image
import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model
model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'best_model.h5'))

# Update these class labels to match your model
class_names = ['Eczema', 'Warts Molluscum ', 'Melanoma', 'Psoriasis pictures Lichen Planus']

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    return img_array

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        save_path = os.path.join(BASE_DIR, 'media', uploaded_file.name)

        with open(save_path, 'wb+') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        img_tensor = preprocess_image(save_path)
        prediction = model.predict(img_tensor)
        label = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        return render(request, 'classifier/upload.html', {
            'prediction': label,
            'confidence': f"{confidence:.2f}",
            'image_url': f"/media/{uploaded_file.name}"
        })

    return render(request, 'classifier/upload.html')