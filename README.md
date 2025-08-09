---
title: Cat vs Dog Classifier
emoji: 🐾
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🐾 Cat vs. Dog Image Classifier API

This project is an end-to-end deep learning application that trains a computer vision model to classify images of cats and dogs, then serves the model via a production-ready REST API.

This project was built as part of my AI Engineer journey and demonstrates the full development lifecycle: from initial experimentation in a Jupyter Notebook to a containerized, deployable web application.

---

## Features
* **Deep Learning Model**: Utilizes a Convolutional Neural Network (CNN) built with the **FastAI** library.
* **REST API**: A robust API built with **FastAPI** to serve the model's predictions.
* **Containerized**: Fully containerized with **Docker** for consistent, reproducible deployments.
* **Interactive Docs**: Automatic API documentation provided by FastAPI at the `/docs` endpoint.

---

## Technologies Used
- **Python 3.11**
- **Deep Learning**: FastAI & PyTorch
- **API**: FastAPI & Uvicorn
- **Containerization**: Docker

---

## Getting Started Locally

### Prerequisites
- Python 3.11
- Docker Desktop

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Murci20965/cat-dog-classifier.git](https://github.com/Murci20965/cat-dog-classifier.git)
    cd cat-dog-classifier
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    .\env\Scripts\activate
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

Once running, the API documentation is available at `http://127.0.0.1:8000/docs`.
