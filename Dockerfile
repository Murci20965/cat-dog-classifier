# Dockerfile

# 1. Use a Python version that matches your development environment
FROM python:3.11-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy and install the project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code and the model file into the container
COPY ./app ./app
COPY cat_dog_classifier_v1.pkl .

# 5. Specify the command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]