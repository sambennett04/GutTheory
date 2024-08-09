# FastAPI
## Build and Run Docker Image
1. Go to README file at ```GutTheory/venv/README.md``` and execute step 2 in the ```Other commands``` section. This will generate a requirements.txt file in ```GutTheory/fastapi``` with the same dependencies specified in venv.
2. To build the docker image run the following command: 
```sh
docker build -t [yourImageName]
```
3. To run your docker image, use:
```sh
docker run -d --name guttheory-fastapi-container -p 80:80 guttheory-fastapi
```
-d: decouples container execution from terminal execution, even if you close out of the terminal the container will still run
-p: sets the port mapping for the local port and the container port

## Other Commands
1. Stop Docker Container
```sh
docker stop [container-name]
```
Exit without a exit code means that the container was exited succesfuly.

2. Remove Docker Container
```sh
docker rm [container-name]
```

3. List All Docker Containers
```sh
docker ps -a
```
Removing the -a in the command shows all running containers.
