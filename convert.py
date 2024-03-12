import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the model from the .pb file
model = tf.saved_model.load('./saved_model.pb')

# Save the model in .h5 format
model.save('ocr_model.h5')