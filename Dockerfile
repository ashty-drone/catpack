FROM sandy1709/catuserbot:slim-buster

# Cloning repo
RUN git clone https://github.com/ashty-drone/nekopack.git -b okteto /root/userbot

# Setting up Working Directory
WORKDIR /root/userbot

# Installing requirements
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Configuring Environment
ENV PATH="/home/userbot/bin:$PATH"

# Copying Directory to image
COPY . .

# Catuserbot!
CMD ["sh","catub"]
