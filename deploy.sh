#! /bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
sudo docker stack deploy --compose-file docker-compose.yaml app
