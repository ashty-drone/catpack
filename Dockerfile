FROM sandy1709/catuserbot:slim-buster

# Cloning-Repo
COPY . .

#Setting up Working Directory

# Installing requirements
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Configuring Environment

# Catuserbot!
CMD ["bash","start"]
