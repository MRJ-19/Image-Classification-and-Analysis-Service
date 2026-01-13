# Image Classification and Analysis Service

This repository contains an image classification service implemented using **Python**, **TensorFlow**, **Computer Vision**, and **FastAPI**.  
The project performs image inference using a pre-trained convolutional neural network and exposes predictions through a REST API.

---

## Repository Contents

### 1. `requirements.txt`

Lists all Python dependencies required to run the project.

Included libraries:
- fastapi
- uvicorn
- tensorflow-cpu
- pillow
- numpy
- python-multipart

Install dependencies:
```
pip install -r requirements.txt
```

---

### 2. Dockerfile

Defines the container configuration for running the application in a Docker environment.

Purpose:
- Creates a reproducible runtime environment
- Installs dependencies from requirements.txt
- Runs the FastAPI application inside a container

Usage (after Dockerfile is finalized):
```
docker build -t image-classifier .
```
```
docker run -p 8000:8000 image-classifier
```

---

### 3. Image Files

chesapeake-bay-retriever-1536x1024.webp  
Sample image file  
Can be used for testing image classification inference  

Golden_retriever.jpg  
Sample image file  
Can be used as an input image for API testing  

Purpose of image files:
- Used to validate model inference
- Helpful for local testing and demonstration

---

## Project Functionality

- Uses a pre-trained CNN model for image classification
- Applies basic image preprocessing:
  - Resizing
  - Normalization
- Returns prediction results via FastAPI REST endpoints
- API responses are returned in structured JSON format

---

## Running the Application (Local)

Install dependencies:
```
pip install -r requirements.txt
```

Start the FastAPI server:
uvicorn main:app --reload

Access the API:
```bash
http://127.0.0.1:8000
```



