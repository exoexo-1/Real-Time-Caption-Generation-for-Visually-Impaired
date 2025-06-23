from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.image import load_img, img_to_array
import pickle
import os

app = Flask(__name__)

# Load tokenizer
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load max_length
max_length = 34  # ← Make sure this matches what you used in training

# Load models
caption_model = tf.keras.models.load_model("model/model.h5")
encoder_model = tf.keras.models.load_model("model/densenet201_encoder.h5")

# Vocabulary index to word mapping
def idx_to_word(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

# Generate caption
def predict_caption(model, feature, tokenizer, max_length):
    in_text = "startseq"
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        y_pred = model.predict([feature, sequence], verbose=0)
        y_pred = np.argmax(y_pred)

        word = idx_to_word(y_pred, tokenizer)
        if word is None:
            break
        in_text += " " + word
        if word == "endseq":
            break
    return in_text.replace("startseq", "").replace("endseq", "").strip()

# Extract features from uploaded image
def extract_features(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    feature = encoder_model.predict(img)
    return feature

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Upload route
@app.route('/generate', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return 'No file part'
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    
    filepath = os.path.join('static', file.filename)
    file.save(filepath)
    
    feature = extract_features(filepath)
    caption = predict_caption(caption_model, feature, tokenizer, max_length)
    
    return render_template('index.html', caption=caption, image_path=filepath)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

