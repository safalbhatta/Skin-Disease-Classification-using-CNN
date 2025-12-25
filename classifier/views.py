from django.shortcuts import render
from django.conf import settings
from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Load model once
model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR, 'best_model.h5'))
class_names = ['Eczema', 'Warts Molluscum ', 'Melanoma', 'Psoriasis pictures Lichen Planus']

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    return img_array

def upload_image(request):
    prediction = None
    confidence = None
    image_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

        # Save image to media folder
        with open(save_path, 'wb+') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # Predict
        img_tensor = preprocess_image(save_path)
        pred = model.predict(img_tensor)
        prediction = class_names[np.argmax(pred)]
        confidence = float(np.max(pred))

        image_url = settings.MEDIA_URL + uploaded_file.name

    return render(request, 'classifier/upload.html', {
        'prediction': prediction,
        'confidence': f"{confidence:.2f}" if confidence else None,
        'image_url': image_url
    })