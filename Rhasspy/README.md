Most of the contents needed to run the voice commands are present in this folder, however, there are a few additional components. The voice models for piper, which can be downloaded [here](https://github.com/rhasspy/piper/blob/master/VOICES.md)
and the piper executable itself which can be downloaded to this directory by calling \
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_arm64.tar.gz \
tar -xvzf piper_arm64.tar.gz \
Once everything is downloaded ensure system has docker installed with\
curl -sSL https://get.docker.com | sh\
Followed by\
sudo usermod -a -G docker $USER\
To add current user to the docker group. Restart your system to enact these changes./
Finally, call ./docker_rebuild.sh to build Rhasspy docker container, which runs immediately in the background. The GUI for customizing Rhasspy is loacated at localhost:12101 on any web browser while the container is running.
