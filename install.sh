#!/bin/sh
sudo docker stop mma-app
sudo docker rm mma-app
sudo docker build -t my_docker_flask:latest .
sudo docker run --name mma-app -d -p 5000:5000 my_docker_flask:latest 



