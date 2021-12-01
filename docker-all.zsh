#!/bin/zsh
git pull
docker build -t alexress/deployress-worker .
docker kill $(docker ps -a -q --filter ancestor=alexress/deployress-worker)
docker run -it --rm -d -p 5005:5005 alexress/deployress-worker
