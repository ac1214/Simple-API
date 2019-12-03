!#/bin/bash

docker build -t flask_server .
docker run --rm -p 80:80 --name instance flask_server
