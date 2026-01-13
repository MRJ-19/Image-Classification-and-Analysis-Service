import io
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load model once at startup
model = MobileNetV2(weights="imagenet")

def analyze_and_predict(image_bytes: bytes):
    # 1. Load and Analyze Metadata
    with io.BytesIO(image_bytes) as buf:
        img = Image.open(buf)
        img.load()  # Load into memory
        
        metadata = {
            "format": img.format or "Unknown",
            "mode": img.mode,
            "size": list(img.size)
        }

        # 2. Preprocessing
        # Ensure image is RGB and resized for MobileNetV2
        img_rgb = img.convert("RGB").resize((224, 224), Image.LANCZOS)
    
    img_array = image.img_to_array(img_rgb)
    img_batch = np.expand_dims(img_array, axis=0)
    processed_data = preprocess_input(img_batch)

    # 3. Inference
    predictions = model.predict(processed_data, verbose=0)
    decoded_results = decode_predictions(predictions, top=3)[0]

    return {
        "analysis": metadata,
        "predictions": [
            {"label": label, "score": round(float(score), 4)} 
            for _, label, score in decoded_results
        ]
    }