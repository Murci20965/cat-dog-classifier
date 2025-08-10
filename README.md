---
title: Cat vs Dog Classifier
emoji: 🐾
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🐾 Cat vs. Dog Image Classifier API + UI

This project is an end-to-end deep learning application that trains a computer vision model to classify images of cats and dogs, then serves the model via a production-ready REST API and an integrated Gradio UI.

This project was built as part of my journey to become an AI Engineer and demonstrates the full development lifecycle: from initial experimentation in a Jupyter Notebook to a containerized, deployable web application.

---

## Features
* **Deep Learning Model**: Utilizes a Convolutional Neural Network (CNN) built with the **FastAI** library.
* **REST API**: A robust API built with **FastAPI** to serve the model's predictions.
* **Gradio UI**: A polished, user-friendly interface available at `/ui` for quick manual testing and demos.
* **Containerized**: Fully containerized with **Docker** for consistent, reproducible deployments.
* **Interactive Docs**: Automatic API documentation provided by FastAPI at the `/docs` endpoint.

---

## Technologies Used
- **Python 3.11**
- **Deep Learning**: FastAI & PyTorch (CPU wheels)
- **API**: FastAPI & Uvicorn
- **UI**: Gradio
- **Containerization**: Docker

---

## Getting Started Locally

### Prerequisites
- Python 3.11
- Docker Desktop

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Murci20965/cat-dog-classifier.git
    cd cat-dog-classifier
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On MacOS/Linux
    source env/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run with Docker (Recommended):**
    Build the Docker image:
    ```bash
    docker build -t cat-dog-classifier .
    ```
    Run the Docker container:
    ```bash
    docker run -p 8000:7860 cat-dog-classifier
    ```

5.  **Run locally without Docker:**
    ```bash
    uvicorn app.main:app --reload
    ```

Once running:
- API docs are available at `http://127.0.0.1:8000/docs`
- Gradio UI is available at `http://127.0.0.1:8000/ui`
- Health check at `http://127.0.0.1:8000/health`

---

## API Summary
- `GET /`: Welcome message
- `GET /health`: Health check
- `POST /predict`: Multipart file upload (field name: `image`). Returns `{ "prediction": "Cat|Dog", "probability": "<float>" }`.

---

## Notes on Model & Environment
- The exported FastAI learner is loaded once at startup for efficiency.
- The container uses CPU-only PyTorch wheels to reduce image size and avoid CUDA dependencies.
- The server binds to `$PORT` if provided (e.g., on Hugging Face Spaces), defaulting to `7860` otherwise.

---

## Hugging Face Spaces
If deploying on Spaces, this repository’s Dockerfile already supports `$PORT`. Ensure the model file `cat_dog_classifier_v1.pkl` is available (Git LFS or Space storage). Rebuild/restart the Space after pushing changes.

---

## License
MIT
