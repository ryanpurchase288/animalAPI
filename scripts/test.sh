#! /bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd app1
pytest --cov ./application 
cd ..
cd app2
pytest --cov ./application 

deactivate

rm -rf venv