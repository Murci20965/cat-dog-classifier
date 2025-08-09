# app/inference.py

import pathlib
from pathlib import Path
from fastai.vision.all import *
import platform

# Handle path differences between Windows and other OSes
# This is a good practice for cross-platform compatibility
plt = platform.system()
if plt == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

# --- Model Loading ---

# Define the path to the model file
# Path(__file__).parent gets the directory of the current script (app/)
# Then we go one level up ('..') to find the .pkl file
model_path = Path(__file__).parent / "../cat_dog_classifier_v1.pkl"

# Load the trained model when the application starts.
# This is efficient because it's done only once.
learn = load_learner(model_path)


# --- Prediction Function ---

def predict_image(image_bytes):
    """
    Takes the bytes of an image file and returns the prediction and probability.
    """
    # Use the loaded learner to predict on the image bytes
    # The predict method returns: (predicted_class, class_index, probabilities)
    prediction, _, probs = learn.predict(image_bytes)

    # Get the highest probability from the list of probabilities
    probability = float(probs.max())

    # The labels are 'False' and 'True' based on our `is_cat` function.
    # We map these to human-readable strings.
    predicted_label = "Cat" if str(prediction) == 'True' else "Dog"

    # Return a clean dictionary result
    return {"prediction": predicted_label, "probability": f"{probability:.4f}"}