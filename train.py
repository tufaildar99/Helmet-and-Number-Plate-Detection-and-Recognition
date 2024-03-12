import os
import random
import string
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras_ocr

# Set GPU memory growth to avoid potential memory errors
physical_devices = tf.config.list_physical_devices("GPU")
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)


def generate_random_string(length=6):
    """Generate a random string of lowercase letters and digits."""
    letters_and_digits = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(length))


def load_license_plate_images(folder_path):
    """Load license plate images from a given folder path."""
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = keras_ocr.tools.read(image_path)
            images.append(image)
            print("Loaded image:", image_path)  # Add this line to print the image paths
    return images


def load_license_plate_text(folder_path):
    """Extract license plate text from file names."""
    text = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            plate_text = os.path.splitext(filename)[0]
            text.append(plate_text)
    return text


def generate_training_data(image_folder):
    """Generate training data by pairing images with their corresponding text labels."""
    images = load_license_plate_images(image_folder)
    text = load_license_plate_text(image_folder)
    print(f"Loaded {len(images)} images and {len(text)} text labels.")

    num_samples = min(len(images), len(text))
    training_data = []

    for i in range(num_samples):
        training_data.append((images[i], text[i]))

    return training_data


def plot_sample(data):
    """Plot an image and its corresponding text label."""
    image, text = data
    plt.imshow(image)
    plt.title("License Plate Text: " + str(text))
    plt.axis("off")
    plt.show()


# Set the path to the folder containing license plate images
image_data_folder = "./TestDataImages"

# Generate training data
training_data = generate_training_data(image_data_folder)

# Display a sample license plate image with its text label
sample_data = random.choice(training_data)
plot_sample(sample_data)

# Initialize the text recognizer
recognizer = keras_ocr.recognition.Recognizer()

# Prepare images for recognition
images = [data[0] for data in training_data]

# Recognize text in the images
pipeline = keras_ocr.pipeline.Pipeline(recognizer=recognizer)
predicted_texts = pipeline.recognize(images=images)

# Compare predicted texts with ground truth
ground_truth_texts = [data[1] for data in training_data]
for predicted_text, ground_truth_text in zip(predicted_texts, ground_truth_texts):
    print(f"Predicted: {predicted_text}, Ground Truth: {ground_truth_text}")

# Save the trained text recognizer model
model_path = "./trained_model"
recognizer.model.save(model_path)
print(f"Trained model saved at: {model_path}")
