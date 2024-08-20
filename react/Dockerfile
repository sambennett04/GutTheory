FROM node:current-alpine

WORKDIR /app

COPY ./app/public/ /app/public
COPY ./app/src/ /app/src
COPY ./app/package.json /app/

#installs all the dependencies specified in package.json
RUN npm install

#specifies the command that will be executed when starting a container from the image
CMD ["npm", "start"]