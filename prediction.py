import numpy as np
from PIL import ImageTk, Image
import tensorflow as tf


def predict():
    # Load the model from the file
    loaded_model = tf.saved_model.load("nn_number_model_mach_2")

    image = Image.open('drawn_grid.png')
    image_array = np.array(image)  # Convert the image to a NumPy array

    # Add a third dimension for RGB channels (assuming the image is in RGB format)
    image_array = np.expand_dims(image_array, axis=2)

    # Resize and preprocess the image
    input_data = tf.image.resize(image_array, [28, 28])  # Resize the image to the model's input size
    input_data = tf.expand_dims(input_data, axis=0)  # Add batch dimension
    input_data = tf.cast(input_data, dtype=tf.float32) / 255.0  # Normalize the image

    # Perform the prediction
    prediction = loaded_model(input_data)

    # Get the predicted label
    predicted_label = tf.argmax(prediction, axis=1).numpy()[0]
    additional_text = str(predicted_label)

    return additional_text
