#!/bin/bash

curl -sSL https://get.docker.com | sh

sudo usermod -a -G docker $USER

# install piper
if [ ! -d piper ]
then
    wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz
    tar -xvzf piper_arm64.tar.gz
fi

# Stop the current Docker container
docker stop rhasspy

docker rm rhasspy

# build a new docker
docker build -t rhasspy .

# run docker
docker run -d -p 12101:12101 \
    --name rhasspy \
    --restart unless-stopped \
    -v "$HOME/.config/rhasspy/profiles:/profiles" \
    -v "/etc/localtime:/etc/localtime:ro" \
    --device /dev/snd:/dev/snd \
    rhasspy \
    --user-profiles /profiles \
    --profile en
