# Exercise 2: Deploy a Flask App on Minikube Using kubectl and YAML

## Objective
To deploy a Python Flask application on Kubernetes using Minikube, Docker, and a YAML configuration file, and access it through a Kubernetes Service.

## Tools Used
- Python
- Flask
- Docker Desktop
- Minikube
- Kubernetes
- kubectl

## Application Details
The Flask application runs on port `15000` and displays the message:

`Hello from Flask on Kubernetes!`

## Procedure

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Create the Flask Application
Created `app.py` using Flask to return a welcome message on port `15000`.

### 3. Create the Docker Image
Created a `Dockerfile` to install Flask and run the application.

Built the image using Minikube:
```bash
minikube image build -t flask-app:latest .
```

### 4. Create the Kubernetes Deployment
Created `flask-deployment.yaml` to define the Flask Deployment with one replica and container port `15000`.

### 5. Deploy the Application
```bash
kubectl apply -f flask-deployment.yaml
```

### 6. Verify the Deployment and Pod
```bash
kubectl get deployments
kubectl get pods -l app=flask-app
```

### 7. Expose the Application
Configured a NodePort Service named `flask-app-service` with service port `15000` and target port `15000`.

### 8. Access the Application
```bash
minikube service flask-app-service --url
```

Opened the generated URL in a browser and verified the Flask welcome message.

## Result
Successfully deployed the Flask application on Minikube and accessed it through a Kubernetes Service.

## Evidence
- `screenshots/` contains screenshots of the Deployment, Pod, and Flask webpage.
- `outputs/` contains Kubernetes command outputs, deployment details, service details, logs, and the service URL.
