# Inference API with Flask, Docker, and CI/CD

This project is a **Flask-based inference API** that can be containerized with **Docker** and supports **NVIDIA CUDA** for GPU-based computations. It includes **CI/CD with GitHub Actions** for automated testing and deployment.

---

## Features  
 **Flask API** with `/predict` endpoint for ML inference  
 **Dockerized** with **CUDA support** for GPU acceleration  
 **CI/CD Pipeline** using **GitHub Actions** for automated builds & testing  
 **Unit Testing** with **Pytest**  

---

# Project Structure

├── app.py              # Flask application
├── tests/              # Unit tests using pytest
│   ├── test_app.py
├── Dockerfile          # Docker setup with CUDA support
├── requirements.txt    # Python dependencies
├── .github/workflows/  # CI/CD pipeline for GitHub Actions
│   ├── docker-ci.yml   # CI/CD workflow
├── README.md           # Project documentation


---

##  Installation  

### **Running Locally (Without Docker)**  
Ensure **Python 3.8+** is installed.

# Clone the repository
git clone https://github.com/ml-deployment.git
cd ml-deployment

# Create a virtual environment (optional but recommended)
python -m venv venv # or use python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask App
python app.py

---

## **Running with Docker**

# Build Docker image
docker build -t inference-app .

# Run the container
docker run --rm -p 5000:5000 inference-app

---

## **Running with GPU(CUDA)**
docker run --rm --gpus all -p 5000:5000 inference-app

---

## *CI-CD Pipeline

Located in .github/workflows/docker-ci.yml, the workflow:

# Runs tests with Pytest
# Builds a Docker image
# Ensures application integrity before deployment



