# Exercise 3: Scaling a Flask App Using ReplicaSets

## Objective
To understand Kubernetes ReplicaSets, scale a Flask application, and observe how Kubernetes maintains the desired number of Pods.

## Real-Life Use Case
During an e-commerce flash sale, website traffic can increase suddenly. Kubernetes ReplicaSets help maintain multiple copies of an application and replace failed or deleted Pods automatically.

## Tools Used
- Python
- Flask
- Docker
- Minikube
- Kubernetes
- kubectl
- YAML

## Application Details
The Flash Sale Flask application provides three endpoints:

- `/` – Displays a welcome message and the Pod name.
- `/buy` – Simulates a purchase and returns the selected product and the Pod handling the request.
- `/health` – Checks the health of the application.

## Procedure

### 1. Create the Flask Application
Created `app.py` using Flask to implement the home, purchase, and health-check endpoints.

### 2. Create the Docker Image
Created a `Dockerfile` to install Flask and Gunicorn and run the application on port `5000`.

Built the image for Minikube:
```bash
minikube image build -t flashsale:1.0 .
```

### 3. Configure the ReplicaSet
Created `flashsale-replicaset.yaml` to define a ReplicaSet with three replicas, health probes, resource limits, and a Kubernetes Service.

### 4. Deploy the Application
```bash
kubectl apply -f flashsale-replicaset.yaml
```

### 5. Verify the ReplicaSet and Pods
```bash
kubectl get rs
kubectl get pods -l app=flashsale
```

Verified that three Pods were created and became ready.

### 6. Scale to Five Replicas
```bash
kubectl scale rs flashsale-rs --replicas=5
```

Checked the updated number of replicas and Pods.

### 7. Test Self-Healing
Deleted one Pod:
```bash
kubectl delete pod <pod-name>
```

Verified that the ReplicaSet automatically created a replacement Pod to maintain five replicas.

### 8. Verify Pod Distribution
```bash
kubectl get pods -o wide
```

Observed that the Pods were running on the single Minikube node.

### 9. Access the Flash Sale Application
```bash
minikube service flashsale-svc --url
```

Accessed the application using the generated URL and tested the purchase endpoint.

## Result
Successfully deployed the Flash Sale Flask application using a Kubernetes ReplicaSet, scaled it from three to five replicas, and verified that a deleted Pod was automatically replaced.

## Evidence
- `screenshots/` contains screenshots of the ReplicaSet, Pods, scaling, Pod replacement, and application responses.
- `outputs/` contains actual Kubernetes command outputs, resource details, node information, and application logs.
