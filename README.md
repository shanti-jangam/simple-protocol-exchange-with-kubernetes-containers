# Simple-Protocol-Exchange-with-Kubernetes-Containers

Assignment 1 – Simple Protocol Exchange


Objective:

The goal is to create a simple message exchange system between containers in a Kubernetes environment using HTTP requests. The application will support both GET and POST requests for interaction and will handle JSON data for communication between the client and server. This system demonstrates basic concepts of containerization, microservices communication, and HTTP request handling.

a.	Requirements:
Following technologies and tools are used to setup and deploy application in Kubernetes
•	Python for the server implementation.
•	Kubernetes for deploying the containerized application.
•	Docker to containerize the Python application.
•	kubectl for managing Kubernetes resources.
•	HTTP GET and POST requests for communication between the client and server.

b.	Steps to be implemented:

1.	Server code(server.py):
The server is responsible for handling incoming GET and POST requests.
Explanation of the server code:
•	GET Request (do_GET): Takes care of GET requests by sending back a fixed JSON response with a basic message. This comes in handy to fetch data from the server.
•	POST Request (do_POST): Receives a JSON payload from the client. It breaks down the JSON and sends back a welcome message making use of the info provided in the request.
•	Running the Server: The server is set up to work on port 8080 and keeps listening for incoming requests non-stop.

2.	Client Code(client.py):
The client continuously sends POST requests to the server and logs the server's responses.
Explanation of the client code:
•	Sends POST requests every 5 seconds to the server.
•	Logs the server's response in the console.

3.	Dockerizing the Application:
After that, we package the Python application in a container to run it on Kubernetes. This means we need to make a Docker file to build an image of the Python application.
Docker File:
•	Base Image: Picking a slim version of Python 3.9 as the starting point.
•	 Copy Files: Moving the project files into the container. 
•	Install Dependencies: Add the Python packages 
•	Expose Port: Open port 8080 so the container can take in requests. 
•	Run Command: When the container starts up, it kicks off server.py.

4.	Building the Docker Image:
Building the docker image using the following commands in the terminal-
docker build -t simple-server -f Dockerfile.server .
docker build -t simple-client -f Dockerfile.client .

Run the image locally to test once the build is completed-
Start the server container:
docker run -p 8080:8080 simple-server
Start the client container:
docker run --network="host" simple-client

c.	Deploying the Application in Kubernetes:

1.	Kubernetes Deployment and Service Configuration for Server: 
Server Configuration (server.yaml):
This file contains both the Deployment and Service configurations required to deploy and expose the server.
Deployment:
•	replicas: Replicas provides load balancing and fault tolerance.
•	selector: Matches Pods labeled with app: simple-server to ensure the deployment only applies to these pods.
•	template:
I.	labels: Assigns the label app: simple-server to the pods, which helps the service route traffic correctly.
II.	containers: Defines the container configuration:
name: simple-server
image: simple-server:latest - Refers to the server docker image built earlier.
ports: Exposes port 8080 in the container for communication.
 Service:
•	selector: Matches pods labeled with app: simple-server so the service routes traffic to the correct pods.
•	ports:
I.	port: Exposes the service on port 80 externally.
II.	targetPort: Forwards incoming traffic from port 80 to port 8080 in the container.
•	type: LoadBalancer ensures the service is accessible outside the Kubernetes cluster by assigning an external IP.
2.	Kubernetes Deployment and Service Configuration for Client:
Client Configuration (client.yaml):
This file contains the Deployment configuration for the client application.
Deployment:
•	replicas: Specifies that one replica of the client application should be created.
•	selector: Matches Pods labeled with app: simple-client to ensure the deployment only applies to these pods.
•	template:
I.	labels: Assigns the label app: simple-client to the pods.
II.	containers: Defines the container configuration:
name: simple-client
image: simple-client:latest - Refers to the client docker image built earlier.

3.	Apply Kubernetes Configurations:
Start minikube:
minikube start
To deploy the application in Kubernetes, run the following commands:
 kubectl apply -f server.yaml
 kubectl apply -f client.yaml

d.	Testing the application:

The server and client are tested after deploying the application using the following commands:
1.	Verify Deployments and Services:
Run the following commands to check the status of pods and services:
kubectl get pods
kubectl get services

2.	Testing GET and POST Requests:
•	Get the External IP: Retrieve the external IP of the server-service:
kubectl get services
•	Test GET Request: Send a GET request to the server:
curl http://<external-ip>/
Response:
{"message": "This is a GET response"}


•	Test POST Request: Send a POST request to the server with a JSON payload:
curl -X POST http://<external-ip>/ -H "Content-Type: application/json" -d '{"name": "Test User"}'
Response:
{"response": "Hello, Test User!"}

Conclusion:

Broadly, this setup demonstrates the entire processing of containerizing, deploying, and exposing a client-server application while ensuring its scalability and visibility from outside using Kubernetes.

