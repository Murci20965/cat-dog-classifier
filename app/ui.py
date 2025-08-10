"""
Gradio UI for Cat vs Dog Classifier

This module builds a Gradio interface that interacts with the FastAPI
endpoint /predict by sending the uploaded image as multipart/form-data.
It is designed to be mounted under the FastAPI app at the /ui route.
"""

# Standard library imports
import io  # Provides in-memory byte streams
import os  # Accesses environment variables such as PORT
from typing import Dict, Tuple  # Provides precise type hints for function signatures

# Third-party imports
import requests  # Performs HTTP requests to the FastAPI backend
from PIL import Image  # Converts PIL Image objects to bytes for HTTP upload
import gradio as gr  # Builds the user interface


def _encode_image_to_bytes(image: Image.Image) -> Tuple[bytes, str]:
    """
    Convert a PIL Image object to PNG-encoded bytes along with the MIME type.

    Parameters
    ----------
    image : PIL.Image.Image
        The image received from Gradio input.

    Returns
    -------
    Tuple[bytes, str]
        A tuple containing the raw PNG bytes and the appropriate MIME type string.
    """
    # Create an in-memory bytes buffer that acts like a file handle
    buffer: io.BytesIO = io.BytesIO()
    # Save the image to the buffer in PNG format to ensure consistent encoding
    image.save(buffer, format="PNG")
    # Retrieve the raw byte content from the buffer
    image_bytes: bytes = buffer.getvalue()
    # Define the correct MIME type for PNG files to inform the server
    mime_type: str = "image/png"
    # Return the bytes and the MIME type together as a tuple
    return image_bytes, mime_type


def _build_api_base_url() -> str:
    """
    Build the base URL for the API within the container environment.

    Returns
    -------
    str
        The base URL string in the form http://127.0.0.1:<port>.
    """
    # Fetch the PORT environment variable, defaulting to 7860 if not present
    port: str = os.environ.get("PORT", "7860")
    # Construct an absolute URL pointing to the local server within the container
    return f"http://127.0.0.1:{port}"


def _call_prediction_api(image: Image.Image) -> Dict[str, str]:
    """
    Send the provided image to the FastAPI /predict endpoint and return the JSON response.

    Parameters
    ----------
    image : PIL.Image.Image
        The image selected by the user in the Gradio interface.

    Returns
    -------
    Dict[str, str]
        The JSON response from the API containing keys such as 'prediction' and 'probability'.
    """
    # Encode the image to PNG bytes and determine the associated MIME type
    image_bytes, mime_type = _encode_image_to_bytes(image)
    # Compose the absolute URL for the prediction endpoint using the locally bound API base
    url: str = f"{_build_api_base_url()}/predict"
    # Prepare the multipart/form-data payload expected by the FastAPI endpoint
    files = {"image": ("upload.png", image_bytes, mime_type)}
    # Execute the POST request to the backend API and capture the HTTP response
    response = requests.post(url, files=files, timeout=30)
    # Raise an exception for any 4xx/5xx HTTP status codes to surface failures
    response.raise_for_status()
    # Parse and return the JSON body of the successful response
    return response.json()


def build_gradio_interface() -> gr.Blocks:
    """
    Construct and return a Gradio Blocks interface tailored for this application.

    Returns
    -------
    gr.Blocks
        The configured Gradio Blocks application ready to be mounted under FastAPI.
    """
    # Select a clean, modern theme to improve aesthetics and readability
    theme = gr.themes.Soft()

    # Create the top-level Blocks container that will hold all UI components
    with gr.Blocks(theme=theme, title="Cat vs Dog Classifier") as demo:
        # Provide a clear header with a concise description of the application
        gr.Markdown("""
        # 🐾 Cat vs Dog Classifier
        Upload an image of a cat or a dog and click Predict. The model API will return the predicted label and probability.
        """)

        # Arrange input and output components side-by-side for better usability
        with gr.Row():
            # Create a column for inputs to group related controls
            with gr.Column():
                # Define an image upload component that accepts common image types and returns a PIL Image
                image_input = gr.Image(label="Upload Image", type="pil")
                # Add a submit button that triggers prediction when clicked
                predict_button = gr.Button(value="Predict", variant="primary")

            # Create a column for outputs to keep results visually organized
            with gr.Column():
                # Display the predicted label in a large, easily readable text box
                prediction_output = gr.Textbox(label="Prediction", interactive=False)
                # Display the probability with a progress-like numeric field
                probability_output = gr.Textbox(label="Probability", interactive=False)

        # Define the function that will be executed when the Predict button is clicked
        def on_predict(image: Image.Image) -> Tuple[str, str]:
            # Call the backend API using the provided image
            result = _call_prediction_api(image)
            # Extract the prediction label string from the result dictionary
            label: str = str(result.get("prediction", "Unknown"))
            # Extract the probability string from the result dictionary
            probability: str = str(result.get("probability", "N/A"))
            # Return both values so they populate the associated Gradio components
            return label, probability

        # Wire the click event to the on_predict function and map inputs/outputs
        predict_button.click(fn=on_predict, inputs=[image_input], outputs=[prediction_output, probability_output])

        # Provide a brief footer with a helpful hint for users
        gr.Markdown("""
        Tip: For best results, use clear photos focused on a single cat or dog.
        """)

    # Return the fully configured Blocks application to the caller for mounting
    return demo 