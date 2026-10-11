# Exercise 4: Docker Networking with Multiple Containers

## Objective
To create a custom Docker bridge network and run multiple containers on the same network. Test connectivity between containers and access a Flask REST API from the host machine.

## Tools Used
- Docker Desktop
- Docker CLI
- Python
- Flask
- MySQL
- Redis
- Windows PowerShell

## Procedure

### 1. Create a Custom Bridge Network
```powershell
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

### 2. Build the Flask API Image
The Flask API provides an `/about` endpoint that returns information in JSON format. The Docker image was built using the provided Dockerfile.

```powershell
docker build -t flask-api .
```

### 3. Run the Containers
```powershell
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabRoot123! mysql:8.0
docker run -d --name redis --network my-bridge-net redis:latest
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### 4. Verify Containers
```powershell
docker ps
```

The Flask, MySQL, and Redis containers were running on the custom bridge network.

### 5. Test the Flask REST API
Open the following URL in a browser:

`http://localhost:5001/about`

The API returns the name, version, and description in JSON format.

### 6. Test Container Connectivity
```powershell
docker exec flask ping -c 4 mysql
docker exec flask ping -c 4 redis
```

The connectivity tests were performed from the Flask container using Docker's container-name DNS resolution.

## Output Evidence
Screenshots and command outputs are saved in the `screenshots` and `outputs` folders.

## Result
A custom Docker bridge network was created, and Flask, MySQL, and Redis containers were run on the network. The Flask REST API was accessed from the host machine, and container connectivity was tested.