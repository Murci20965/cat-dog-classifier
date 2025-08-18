---
title: Cat vs Dog Classifier
emoji: 🐾
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🐾 Cat vs. Dog Image Classifier

[![Python](https://img-shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![FastAI](https://img-shields.io/badge/FastAI-2.7%2B-red?logo=fastai)](https://docs.fast.ai/)
[![FastAPI](https://img-shields.io/badge/FastAPI-Ready-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img-shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img-shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An **end-to-end** deep learning application that classifies images of cats and dogs.  
This project demonstrates the full MLOps lifecycle, from training a model with **FastAI** to deploying it as a containerized web application with **FastAPI** and a **Gradio** user interface.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Deployment](#deployment)
- [License](#license)

---

## 📖 Overview
This project was built to practice and document the process of taking a machine learning model from a research notebook to a production-ready service. It uses a Convolutional Neural Network (CNN) trained with the FastAI library to achieve high accuracy in classifying images of cats and dogs. The trained model is then served via a high-performance REST API and a user-friendly web interface.

---

## ✨ Features
✅ **High-Performance Model** – A CNN trained with the high-level FastAI library.  
✅ **RESTful API** – Built with FastAPI for scalable, asynchronous inference.  
✅ **Interactive UI** – A simple, user-friendly interface built with Gradio.  
✅ **Dockerized** – Fully containerized with Docker for reproducible, one-command deployments.  
✅ **MLOps-Ready** – A clean, modular structure that separates concerns and is ready for cloud deployment.

---

## 📂 Dataset
**Source:** [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)  
**Content:** A 37-category pet dataset with approximately 200 images for each class. This project specifically uses the "Cat" and "Dog" images.  
**Training:** The model training process is documented in the Jupyter Notebook located in the `notebooks/` directory.

---

## 🛠 Tech Stack
- **Backend:** Python, FastAPI, Uvicorn  
- **Deep Learning:** FastAI, PyTorch (CPU)  
- **UI:** Gradio  
- **Containerization:** Docker  

---

## Project Architecture
The project follows a modular structure for a clean separation of concerns:
```
cat-dog-classifier/
│
├── app/              # FastAPI backend source code
│   ├── inference.py  # Core prediction logic
│   ├── main.py       # API routes
│   └── ui.py         # Gradio UI definition
│
├── notebooks/        # Jupyter notebook for model training
│
├── .dockerignore     # Specifies files to ignore in the Docker build
├── .gitattributes    # Git LFS configuration
├── .gitignore        # Specifies files to ignore for Git
├── Dockerfile        # Recipe for building the application container
├── LICENSE
├── README.md         # Project documentation
├── cat_dog_classifier_v1.pkl # The trained model file
└── requirements.txt  # Project dependencies
```
---

## Setup and Installation

Follow these steps to set up the project on your local machine.

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/Murci20965/cat-dog-classifier.git](https://github.com/Murci20965/cat-dog-classifier.git)
   cd cat-dog-classifier
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---
## Usage Guide

Ensure your virtual environment is active before running any commands.

### 1. Running the Application (Local)

To run the unified FastAPI server and Gradio UI locally, use the following command:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- The **Gradio UI** will be available at `http://127.0.0.1:8000/`
- The **API documentation** will be available at `http://127.0.0.1:8000/docs`

### 2. Running with Docker

Ensure Docker Desktop is installed and running.

1. **Build the Docker image:**

   ```bash
   docker build -t cat-dog-classifier .
   ```

2. **Run the container:**

   ```bash
   docker run -p 8000:8000 --name cat-dog-app cat-dog-classifier
   ```
   The application will be running inside the container and accessible at `http://localhost:8000`.

---
## Deployment

This application is fully containerized and ready for deployment. The `Dockerfile` can be used to deploy the application to any cloud service that supports containers, such as Hugging Face Spaces, AWS, Azure, or Google Cloud Platform.

---
## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
