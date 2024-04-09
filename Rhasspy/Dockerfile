# Use the Rhasspy base image
FROM rhasspy/rhasspy

WORKDIR /home

# update profile.json
COPY profile.json ../profiles/en

# Add Piper TTS
COPY piper ./piper
COPY voice_models ./voice_models

COPY ./pass_on.py ./piper
