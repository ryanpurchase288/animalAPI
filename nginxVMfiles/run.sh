#! /bin/bash
docker run -d -p 80:80 --name nginx-swarm-ingress --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine