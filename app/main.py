# app/main.py

from fastapi import FastAPI, UploadFile, File
from .inference import predict_image # Use a relative import

# Create the FastAPI app object
app = FastAPI(
    title="Cat vs. Dog Classifier API",
    description="An API to classify images as either a cat or a dog.",
    version="1.0.0"
)

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome! Navigate to /docs to test the API."}


# Define the prediction endpoint
@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    """
    Accepts an image file, gets a prediction, and returns the result.
    """
    # Read the image file as bytes
    image_bytes = await image.read()

    # Get the prediction from our inference function
    prediction_result = predict_image(image_bytes)

    # Return the result
    return prediction_result