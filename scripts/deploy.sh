#! /bin/bash
docker-compose pull
sudo docker stack deploy --compose-file docker-compose.yaml animalApp
