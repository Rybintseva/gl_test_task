#!/bin/bash

docker build -t ubuntu_test_image .

docker run --name test_container -i ubuntu_test_image

docker cp test_container:/gl_test_task/report.html  ./
docker stop test_container
docker rm test_container
