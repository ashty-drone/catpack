FROM sandy1709/catuserbot:slim-buster

# Cloning source code
COPY . .

# Installing Okteto CLI
RUN curl https://get.okteto.com -sSfL | sh

# Installing requirements
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Catuserbot!
CMD ["bash","start"]
