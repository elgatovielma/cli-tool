# Specify base NodeJs image
FROM node

# Directory where to work
RUN mkdir -p /usr/src/app
WORKDIR '/usr/src/app'

# Install some dependencies
COPY ./package*.json ./
RUN npm install
RUN apt-get update || : && apt-get install python -y
COPY . .

EXPOSE 8080

# Default command
CMD [ "node", "server.js" ]