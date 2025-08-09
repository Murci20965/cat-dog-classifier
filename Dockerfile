# Dockerfile

# 1. Use a Python version that matches your development environment
FROM python:3.11-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Install system dependencies needed for image processing
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy and install the project dependencies
COPY requirements.txt .

# Pre-install CPU-only torch and torchvision from the official CPU wheel index to avoid CUDA downloads
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu torch==2.3.1+cpu torchvision==0.18.1+cpu \
    && pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# 5. Copy the application code and the model file into the container
COPY ./app ./app
COPY cat_dog_classifier_v1.pkl .

# 6. Expose default app port (optional)
EXPOSE 7860

# 7. Specify the command to run when the container starts; honor $PORT for platforms like Hugging Face Spaces
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-7860}"]