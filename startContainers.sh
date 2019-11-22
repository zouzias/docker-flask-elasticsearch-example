#!/bin/bash

# If DOCKER_MACHINE_IP is not set, you need to set it manually before running docker-compose up
export DOCKER_MACHINE_IP=$(docker-machine ip)

echo "**********************************************************************"
echo "**********************************************************************"
echo "Browse to http://${DOCKER_MACHINE_IP}:5000/info to check Elastic status"
echo "**********************************************************************"
echo "**********************************************************************"


docker-compose up
