# app/inference.py

import pathlib
from pathlib import Path
from fastai.vision.all import *
import platform
from io import BytesIO
from fastai.vision.core import PILImage
import sys
import types

# Inject a minimal shim for environments where a training-time module is missing
# This helps unpickling if the export referenced a module named 'fasttransform'
if 'fasttransform' not in sys.modules:
    pkg = types.ModuleType('fasttransform')
    # Mark as a package so that 'fasttransform.transform' can be imported
    pkg.__path__ = []  # type: ignore[attr-defined]
    sys.modules['fasttransform'] = pkg

# Ensure the submodule exists with a basic Transform and Pipeline symbols
if 'fasttransform.transform' not in sys.modules:
    from fastcore.transform import Transform as _FC_Transform, Pipeline as _FC_Pipeline

    sub = types.ModuleType('fasttransform.transform')
    sub.Transform = _FC_Transform
    sub.Pipeline = _FC_Pipeline
    sys.modules['fasttransform.transform'] = sub

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

# A fallback label function sometimes referenced in exported learners
def is_cat(x):
    try:
        name = x.name if hasattr(x, 'name') else str(x)
        return name[0].isupper()
    except Exception:
        return False

# Load the trained model when the application starts.
# This is efficient because it's done only once.
learn = load_learner(model_path)


# --- Prediction Function ---

def predict_image(image_bytes: bytes) -> dict:
    """
    Takes the bytes of an image file and returns the prediction and probability.
    """
    # Decode bytes into a PIL image expected by fastai's Learner.predict
    try:
        image = PILImage.create(BytesIO(image_bytes))
    except Exception as exc:
        raise ValueError("Invalid image data. Ensure you upload a valid image file.") from exc

    prediction, _, probs = learn.predict(image)

    probability = float(probs.max())

    predicted_label = "Cat" if str(prediction) == 'True' else "Dog"

    return {"prediction": predicted_label, "probability": f"{probability:.4f}"}