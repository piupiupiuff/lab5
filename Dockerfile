#1
FROM node:16 AS builder
WORKDIR /usr/src/app
COPY . .
RUN npm install && \
    npm run build
ARG DOCKER_HUB_USERNAME
ARG DOCKER_HUB_PASSWORD
RUN echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin && \
    docker build -t $DOCKER_HUB_USERNAME/my-node-app . && \
    docker push $DOCKER_HUB_USERNAME/my-node-app
#2
FROM node:16 AS tester
RUN npm install -g mocha
WORKDIR /usr/src/app
ARG DOCKER_HUB_USERNAME
COPY --from=builder /usr/src/app .
CMD ["npm", "test"]
