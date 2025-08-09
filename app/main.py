# app/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .inference import predict_image  # Use a relative import

# Create the FastAPI app object
app = FastAPI(
    title="Cat vs. Dog Classifier API",
    description="An API to classify images as either a cat or a dog.",
    version="1.0.0"
)

# Enable permissive CORS for easy testing from browsers/tools
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome! Navigate to /docs to test the API."}

# Simple health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Define the prediction endpoint
@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    """
    Accepts an image file, gets a prediction, and returns the result.
    """
    # Basic validation for image content type
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid content type. Please upload an image file.")

    try:
        image_bytes = await image.read()
        prediction_result = predict_image(image_bytes)
        return prediction_result
    except ValueError as ve:
        # Raised when the file cannot be decoded as an image
        raise HTTPException(status_code=400, detail=str(ve)) from ve
    except Exception as exc:
        # Unexpected errors
        return JSONResponse(status_code=500, content={"detail": "Internal server error during prediction."})